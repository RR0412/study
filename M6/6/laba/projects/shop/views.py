from django.shortcuts import render

def products_view(request):
    return render(request, 'shop/products_view.html')
