from django.shortcuts import render

def index(request):
    return render(request, 'shop/index.html')

def products_view(request):
    return render(request, 'shop/products.html')

def product_add_view(request):
    return render(request, 'shop/product_add.html')

def product_view(request):
    return render(request, 'shop/product.html')

def category_add_view(request):
    return render(request, 'shop/category_add.html')