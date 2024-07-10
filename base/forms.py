from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from base.models import Product
from django.contrib.auth.forms import AuthenticationForm

class ProductForm(forms.ModelForm):
    sizes = forms.MultipleChoiceField(
        choices=Product.SIZE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'description-textarea',
        })
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'name-input',  
        })
    )
    class Meta:
        model = Product
        fields = '__all__'

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Hide help text for username field
        self.fields['username'].help_text = ''
        
        # Hide all password validation messages
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['password'].label = ''
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control'
    }))
class AddToCartForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput)
    quantity = forms.IntegerField(min_value=1, initial=1)    
    
