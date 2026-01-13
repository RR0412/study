from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Category,Product
from datetime import datetime

def index(request):
    return render(request, 'shop/index.html')

def products_view(request):
    products = Product.objects.all()
    return render(request, 'shop/products.html', {'products': products})


def product_add_view(request):
    if request.method == 'GET':
        return render(request, 'shop/product_add.html')
    # elif request.method == 'POST':


def product_view(request,pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product.html', context={'product': product})

def category_add_view(request):
    return render(request, 'shop/category_add.html')