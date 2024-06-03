from django import forms

from base.models import ArrivalProduct, Product


class ArrivalProductForm(forms.ModelForm):
    class Meta:
        model = ArrivalProduct
        fields = ['product_name', 'product_image', 'product_price']
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image1', 'image2', 'price', 'category']
