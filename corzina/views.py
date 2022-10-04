from django.shortcuts import render

from corzina.models import Category, Product

app_name = 'corzina'


def get_category(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'category.html', context)


def get_product(request, slug):
    products = Product.objects.filter(category__slug=slug)
    context = {'products': products}
    return render(request, 'products.html', context)
