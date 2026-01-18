from django.shortcuts import render,get_object_or_404
from django.core import serializers
from django.http import HttpResponse,HttpResponseNotAllowed,JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from api.models import Product,CATEGORY_CHOICES
from django.forms.models import model_to_dict
import json



def products_view(request,*args,**kwargs):
    if request.method == 'GET':
        products = Product.objects.all().order_by('-category','-name')
        answer_list = []
        for product in products:
            answer = {
            'name' : product.name,
            'price': str(product.price),
            'category' : product.category
            }
            answer_list.append(answer)
        return JsonResponse(answer_list, safe=False)
    elif request.method == 'POST':
        try:
            product_data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        product = Product.objects.create(
            name=product_data['name'],
            description=product_data.get('description') or None,
            category=product_data['category'],
            quantity=product_data['quantity'],
            price=product_data['price'],
        )
        return JsonResponse({"id": product.pk}, status=201)
        
    
@ensure_csrf_cookie
def get_token_view(request,*args,**kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])

def product_detail_view(request,pk,*args,**kwargs):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'PUT':
        product_data = json.loads(request.body)
        fields = {'name', 'description', 'category', 'quantity', 'price'}
        if product_data['category'] not in dict(CATEGORY_CHOICES):
            return JsonResponse({"error": "Wrong category"}, status=400)
        request_fields = set(product_data.keys())
        if request_fields != fields:
            return JsonResponse({"error": "Fields mismatch"},status=400)
        product.name = product_data['name']
        product.description = product_data['description'] or None
        product.category = product_data['category']
        product.quantity = product_data['quantity']
        product.price = product_data['price']
        product.save()
        return HttpResponse(status=204)
    
    elif request.method == 'PATCH':
        product_data = json.loads(request.body)
        fields = ['name', 'description', 'category', 'quantity', 'price']
        for key, value in product_data.items():
            if key not in fields:
                continue
            if key == 'category':
                if value not in dict(CATEGORY_CHOICES):
                    return JsonResponse({"error": "Wrong category"},status=400)             
            setattr(product, key, value)
        product.save()
        return HttpResponse(status=204)

    elif request.method == 'DELETE':
        if request.GET.get("confirm") != "true":
            return JsonResponse(
                {"error": "Deletion not confirmed"},
                status=400
            )
        product.delete()
        return HttpResponse(status=204)
    
    return JsonResponse({"error": "Method not allowed"}, status = 405)
    


