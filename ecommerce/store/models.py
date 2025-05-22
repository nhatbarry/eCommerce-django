from django.db import models

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, default='unknown')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    price = models.BigIntegerField()

    image = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        verbose_name_plural = 'products'
    
    def __str__(self):
        return self.title
