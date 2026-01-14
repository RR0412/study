from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Category,Product
from datetime import datetime

def index(request):
    return render(request, 'shop/index.html')

def products_view(request):
    products = Product.objects.all()
    return render(request, 'shop/products.html', {'products': products})


def category_add_view(request):
    if request.method == 'GET':
        return render(request, 'shop/category_add.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description') or None
        Category.objects.create(name=name, description=description)
        return redirect('products')
    
def product_add_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'shop/product_add.html',{'categories': categories})
    elif request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.POST.get('image') or None
        category_id = request.POST.get('category')
        if category_id:
            category = Category.objects.get(pk=category_id)
        else:
            category = None
        description = request.POST.get('description') or None
        product=Product.objects.create(name=name, price=price,
                               image=image,
                               category=category,
                               description=description)
        categories = Category.objects.all()
        return redirect('product',pk=product.pk)


def product_view(request,pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product.html', context={'product': product})

def categories_view(request):
    categories= Category.objects.all()
    return render(request,'shop/categories.html', {'categories': categories})


def category_delete_view(request,pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('categories')   
    return render(request, 'shop/category_confirm_delete.html',
                  {'category': category})

def category_edit_view(request,pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category.name = name
        category.description = description or None
        category.save()
        return redirect('categories')
    return render(request, 'shop/category_edit.html',
                  {'category': category})

def product_delete_view(request,pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    return render (request,'shop/product_confirm_delete.html',
                   {'product': product})
