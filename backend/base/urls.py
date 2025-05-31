from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('prods/', views.getProds, name='prods'),
    path('prod/<str:pk>/', views.getProd, name='prod'),
]
