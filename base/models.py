from django.db import models
from django.contrib.auth.models import User  # Import the User model


# Create your models here.
class ArrivalProduct(models.Model):
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='arrival_product_images/')
    product_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image1 = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/', blank=True, null=True)  # Optional second image
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, choices=(
        ('Tops', 'Tops'),
        ('Bottoms', 'Bottoms'),
        ('Outwear', 'Outwear'),
        ('Accessories', 'Accessories'),
        ('Suits', 'Suits'),
        ('Footwear', 'Footwear'),
        ('Undergarments', 'Undergarments'),
    ))

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"Cart for {self.user.username}"
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    