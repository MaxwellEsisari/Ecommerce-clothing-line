from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop_here/', views.shop_here, name='shop_here'),
    path('add-products/', views.add_products, name='add_products'),
    path('add-products/<int:product_id>/', views.add_products, name='edit_product'),
    
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),  # Add this line
    path('collections/', views.collections, name='collections'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),
    path('users/', views.users, name='users'),
    path('customers/', views.customers, name='customers'),
    path('reports/', views.reports, name='reports'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('upload-arrival-product/', views.upload_arrival_product, name='upload_arrival_product'),
    path('arrival-product-list/', views.arrival_product_list, name='arrival_product_list'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
  


]
