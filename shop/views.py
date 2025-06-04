from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

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

