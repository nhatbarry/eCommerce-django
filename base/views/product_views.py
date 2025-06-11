from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from rest_framework import status

from base.models import Product, Review, Brand, Category
from base.serializers import (
    ProductSerializer, BrandSerializer, CategorySerializer
)


@api_view(['GET'])
def getProducts(request):
    query = request.query_params.get('keyword', '')
    products = Product.objects.filter(name__icontains=query).order_by('-createdAt')

    page = request.query_params.get('page')
    paginator = Paginator(products, 5)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    page = int(page) if page else 1

    serializer = ProductSerializer(products, many=True, context={'request': request})
    return Response({'products': serializer.data, 'page': page, 'pages': paginator.num_pages})


@api_view(['GET'])
def getTopProducts(request):
    products = Product.objects.filter(rating__gte=4).order_by('-rating')[:5]
    serializer = ProductSerializer(products, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = get_object_or_404(Product, _id=pk)
    serializer = ProductSerializer(product, context={'request': request})
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createProduct(request):
    user = request.user
    brand = Brand.objects.first()
    category = Category.objects.first()

    product = Product.objects.create(
        user=user,
        name='Sample Name',
        price=0,
        brand=brand,
        countInStock=0,
        category=category,
        description=''
    )

    serializer = ProductSerializer(product, context={'request': request})
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateProduct(request, pk):
    data = request.data
    product = get_object_or_404(Product, _id=pk)

    brand = get_object_or_404(Brand, _id=data['brand']) if isinstance(data['brand'], int) else Brand.objects.filter(brand=data['brand']).first()
    category = get_object_or_404(Category, _id=data['category']) if isinstance(data['category'], int) else Category.objects.filter(category=data['category']).first()

    product.name = data['name']
    product.price = data['price']
    product.brand = brand
    product.countInStock = data['countInStock']
    product.category = category
    product.description = data['description']
    product.save()

    serializer = ProductSerializer(product, context={'request': request})
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteProduct(request, pk):
    product = get_object_or_404(Product, _id=pk)
    product.delete()
    return Response('Product Deleted')


@api_view(['POST'])
def uploadImage(request):
    data = request.data
    product = get_object_or_404(Product, _id=data['product_id'])

    product.image = request.FILES.get('image')
    product.save()

    return Response('Image was uploaded')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createProductReview(request, pk):
    user = request.user
    product = get_object_or_404(Product, _id=pk)
    data = request.data

    if product.review_set.filter(user=user).exists():
        return Response({'detail': 'Product already reviewed'}, status=status.HTTP_400_BAD_REQUEST)

    if data.get('rating', 0) == 0:
        return Response({'detail': 'Please select a rating'}, status=status.HTTP_400_BAD_REQUEST)

    Review.objects.create(
        user=user,
        product=product,
        name=user.first_name,
        rating=data['rating'],
        comment=data['comment'],
    )

    reviews = product.review_set.all()
    product.numReviews = reviews.count()
    product.rating = sum([r.rating for r in reviews]) / reviews.count()
    product.save()

    return Response('Review Added')


@api_view(['GET'])
def getBrands(request):
    keywords = request.query_params.getlist('keyword')

    if keywords:
        query = Q()
        for word in keywords:
            query |= Q(brand__icontains=word)
        brands = Brand.objects.filter(query)
    else:
        brands = Brand.objects.all()

    serializer = BrandSerializer(brands, many=True)
    return Response({'brands': serializer.data})


@api_view(['GET'])
def getCategories(request):
    keywords = request.query_params.getlist('keyword')

    if keywords:
        query = Q()
        for word in keywords:
            query |= Q(category__icontains=word)
        categories = Category.objects.filter(query)
    else:
        categories = Category.objects.all()

    serializer = CategorySerializer(categories, many=True)
    return Response({'categories': serializer.data})
