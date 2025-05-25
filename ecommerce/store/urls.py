from django.urls import path

from . import views

urlpatterns = [
    #main page
    path('', views.store, name='store'),
    #product
    path('product/<slug:product_slug>', views.product_info, name='product-info'),
    #category
    path('search/<slug:category_slug>', views.list_category, name='list-category'),
]
