from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Tops', 'Tops'),
        ('Bottoms', 'Bottoms'),
        ('Outwear', 'Outwear'),
        ('Accessories', 'Accessories'),
        ('Suits', 'Suits'),
        ('Footwear', 'Footwear'),
        ('Undergarments', 'Undergarments'),
    ]

    SIZE_CHOICES = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large'),
        ('XXXL', 'Triple Extra Large'),
        ('30', '30'),
        ('31', '31'),
        ('32', '32'),
        ('33', '33'),
        ('34', '34'),
        ('35', '35'),
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField(default=0, null=False, blank=False)

    image1 = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/', blank=True, null=True)
    image3 = models.ImageField(upload_to='products/', blank=True, null=True)
    image4 = models.ImageField(upload_to='products/', blank=True, null=True)
    image5 = models.ImageField(upload_to='products/', blank=True, null=True)

    last_updated = models.DateTimeField(auto_now=True)

    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    sizes = models.CharField(max_length=200, blank=True)  # To store comma-separated sizes

    def save(self, *args, **kwargs):
        if isinstance(self.sizes, list):
            self.sizes = ",".join(self.sizes)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')
    size = models.CharField(max_length=10)  # Add this line
    quantity = models.PositiveIntegerField(default=1)



    def __str__(self):
        return f'Cart for {self.user.username}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=10)  # Add this line


    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
    
class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    response_data = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.amount}"    