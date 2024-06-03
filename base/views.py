from django.shortcuts import  get_object_or_404, render,redirect
from .forms import ArrivalProductForm, ProductForm
from .models import ArrivalProduct, Cart, CartItem, Product



def upload_arrival_product(request):
    if request.method == 'POST':
        form = ArrivalProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Form saved successfully")
            return redirect('arrival_product_list')
        else:
            print("Form is not valid")
            print(form.errors)  # Print form errors to identify the specific validation issues
    else:
        form = ArrivalProductForm()
    return render(request, 'base/upload_arrival_product.html', {'form': form})

def arrival_product_list(request):
    arrival_products = ArrivalProduct.objects.all()
    return render(request, 'base/arrival_product_list.html', {'arrival_products': arrival_products})


def index(request):
    # Fetch arrival products from the database
    arrival_products = ArrivalProduct.objects.all()

    # Pass arrival_products to the template context
    return render(request, 'base/index.html', {'arrival_products': arrival_products})

def shop_here(request):
    # Retrieve all products from the database
    products = Product.objects.all()

    # Organize products into categories
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

def add_products(request):
    if request.method == 'POST':
        # If the form has been submitted
        form = ProductForm(request.POST, request.FILES)  # If you have a form
        if form.is_valid():
            form.save()
            return redirect('shop_here')  # Redirect to the shop_here page after adding the product
    else:
        # If it's a GET request, display the form
        form = ProductForm()  # If you have a form

    return render(request, 'base/add_products.html', {'form': form})

def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'base/product_details.html', {'product': product})

def cart(request):
    
    return render(request, 'base/cart.html')

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')


def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'base/cart.html', {'cart_items': cart_items, 'total_price': total_price})

