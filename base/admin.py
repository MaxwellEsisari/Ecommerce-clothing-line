from django.contrib import admin
from .models import  Cart, Product, CartItem, Payment


admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Payment)




