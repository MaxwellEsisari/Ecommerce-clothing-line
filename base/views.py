from email.message import EmailMessage
from gc import get_count
import json
from django.shortcuts import  get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from westside import settings
from .forms import ProductForm, SignUpForm
from .models import   Cart, CartItem, Product
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from .forms import SignUpForm
from django.template.loader import render_to_string
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login, authenticate
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import base64
import requests
from requests.auth import HTTPBasicAuth
from .models import Payment

def upload_arrival_product(request):
    # if request.method == 'POST':
    #     form = ArrivalProductForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         print("Form saved successfully")
    #         return redirect('arrival_product_list')
    #     else:
    #         print("Form is not valid")
    #         print(form.errors)  # Print form errors to identify the specific validation issues
    # else:
    #     form = ArrivalProductForm()
    return render(request, 'base/upload_arrival_product.html')

def arrival_product_list(request):
    # arrival_products = ArrivalProduct.objects.all()
    return render(request, 'base/arrival_product_list.html')


def index(request):
    # Fetch arrival products from the database
    # arrival_products = ArrivalProduct.objects.all()

    # Pass arrival_products to the template context
    return render(request, 'base/index.html')

def shop_here(request):
    products = Product.objects.all()
    categories = {}
    for product in products:
        if product.category not in categories:
            categories[product.category] = [product]
        else:
            categories[product.category].append(product)

    context = {
        'categories': categories

    }
    return render(request, 'base/shop_here.html', context)

def add_products(request, product_id=None):
    if product_id:
        product = get_object_or_404(Product, pk=product_id)
    else:
        product = None

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            sizes = request.POST.getlist('sizes')
            product.sizes = ','.join(sizes)
            product.save()
            return redirect('shop_here')
        else:
            # Print form errors to console for debugging
            print(form.errors)
    else:
        form = ProductForm(instance=product)

    return render(request, 'base/add_products.html', {'form': form})

def collections(request):
    products = Product.objects.all()
    categories = {}
    for product in products:
        if product.category not in categories:
            categories[product.category] = [product]
        else:
            categories[product.category].append(product)
    
    context = {
        'categories': categories
    }
    return render(request, 'base/collections.html', context)


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    sizes = product.sizes.split(',')  # Split sizes into a list
    if request.method == 'POST':
        size = request.POST.get('size')
        quantity = int(request.POST.get('quantity', 1))
        return add_to_cart(request, product_id, size, quantity)
    return render(request, 'base/product_details.html', {'product': product, 'sizes': sizes})

def dashboard(request):
    user_count = User.objects.all().count()  # Calculate total number of users
    
    context = {
        'user_count': user_count,
    }
    
    return render(request, 'base/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    categories = {}
    for product in products:
        if product.category not in categories:
            categories[product.category] = [product]
        else:
            categories[product.category].append(product)
    
    context = {
        'categories': categories
    }
    
    return render(request, 'base/products.html', context)

def orders(request):
    
    return render(request, 'base/orders.html')

def users(request):
    users = User.objects.all()
    user_count = users.count()  # Calculate the count of users

    context = {
        'users': users,
        'user_count': user_count, 
        }
    return render(request, 'base/users.html', context)

def customers(request):
    
    return render(request, 'base/customers.html')

def reports(request):
    
    return render(request, 'base/reports.html')

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.product.selling_price * item.quantity for item in cart_items)
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'base/cart.html', context)

def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.product.selling_price * item.quantity for item in cart_items)
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total_price': total_price,
    }
   
    return render(request, 'base/checkout.html', context)

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        size = request.POST.get('selected_size')  # Get selected size from POST data
        quantity = int(request.POST.get('quantity', 1))  # Get quantity from POST data, default to 1
        
        # Get or create the user's cart
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        # Check if the item is already in the cart
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, size=size)
        
        if not created:
            # If item already exists in cart, increment quantity
            cart_item.quantity += quantity
            cart_item.save()
        else:
            # If new item added to cart, set quantity
            cart_item.quantity = quantity
            cart_item.save()
    
    return redirect('view_cart')

@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    
    return redirect('checkout')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Send confirmation email
            subject = 'Welcome to MySite'
            message = render_to_string('base/emails.html', {
                'username': user.username,
            })
            email = EmailMessage(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [user.email],
            )
            email.content_subtype = "html"  # Main content is now text/html
            email.send()
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'base/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'base/login.html', {'form': form})

def logout_view(request):
    django_logout(request)
    return redirect('index')

@require_http_methods(["DELETE"])
def delete_product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        product.delete()
        return JsonResponse({'message': 'Product deleted successfully.'}, status=204)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
