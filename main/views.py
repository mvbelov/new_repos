from django.shortcuts import render, redirect

# Create your views here.
from main.models import Product, Category


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def get_category(request, id):
    categories = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'main/index.html', context)
