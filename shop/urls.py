from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('accounts/register/', views.register, name='register'),
]