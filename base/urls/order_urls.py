from django.urls import path
from base.views import order_views as views


urlpatterns = [

    path('', views.getOrders, name='orders'),
    path('addtocart/<str:pk>/', views.addToCart, name='add-to-cart'),
    path('makeorder/', views.makeOrder, name='make-order'),
    path('myorders/', views.getMyOrders, name='myorders'),
    path('cart/', views.getCart, name='cart'),

    path('<str:pk>/deliver/', views.updateOrderToDelivered, name='order-delivered'),

    path('<str:pk>/', views.getOrderById, name='user-order'),
    path('<str:pk>/pay/', views.updateOrderToPaid, name='pay'),
]
