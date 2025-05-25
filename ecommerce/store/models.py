from django.db import models

from django.urls import reverse

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("list-category", args=[self.slug])
    

def product_image_upload_path(instance, filename):
    return f'images/{instance.title}/{filename}'


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, default='unknown')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    price = models.BigIntegerField()

    image = models.ImageField(upload_to=product_image_upload_path, blank=True)

    class Meta:
        verbose_name_plural = 'products'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("product-info", args=[self.slug])
    
