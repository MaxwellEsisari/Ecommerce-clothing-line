from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.index, name="index"),
    path('upload-arrival-product/', views.upload_arrival_product, name='upload_arrival_product'),
    path('arrival_product_list/', views.arrival_product_list, name='arrival_product_list'),
    path('shop_here/', views.shop_here, name='shop_here'),
    path('add_products/', views.add_products, name='add_products'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('carts/', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),


]