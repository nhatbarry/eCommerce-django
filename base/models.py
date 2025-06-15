from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Brand(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    brand = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.brand

class Category(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    category = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.category

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True, default='/placeholder.png')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    _id = models.AutoField(primary_key=True, editable=False)

    ram = models.IntegerField(null=True, blank=True)
    screen_size = models.DecimalField(decimal_places=1, null=True, max_digits=3)
    processor = models.CharField(max_length=100, null=True, blank=True)
    gpu_brand = models.CharField(max_length=100, null=True, blank=True)
    DRIVE_SIZE_CHOICES = [
        (16, '16 GB'),
        (32, '32 GB'),
        (64, '64 GB'),
        (128, '128 GB'),
        (256, '256 GB'),
        (512, '512 GB'),
        (1024, '1 TB'),
    ]

    drive_size = models.IntegerField(choices=DRIVE_SIZE_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.name



class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.rating)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    receiver = models.CharField(max_length=200, null=True, blank=True)
    taxPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    shippingPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    totalPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.createdAt)
    

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name='cart')
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        if self.user:
            return f"{self.user.username}'s cart"
        return "No user cart"



class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    discount = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True, default=0)
    image = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class ShippingAddress(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.address)
