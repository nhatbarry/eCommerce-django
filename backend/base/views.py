from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .products import products

# Create your views here.
@api_view(['GET'])
def getRoutes(request):

    return Response('Helo')

@api_view(['GET'])
def getProd(request, pk):
    for prod in products:
        if prod['_id'] == pk:
            product = prod


    return Response(product)

@api_view(['GET'])
def getProds(request):
    return Response(products)