from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Cart, CartItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def home(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    return render(request, 'shop/home.html', {'products': products, 'categories': categories})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    comments = product.comments.filter(approved=True)
    return render(request, 'shop/product_detail.html', {'product': product, 'comments': comments})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #user = form.save()
           # login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'shop/cart_detail.html', {'cart': cart})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('shop:cart_detail')

