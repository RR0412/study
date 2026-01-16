from django.shortcuts import render,get_object_or_404
from django.core import serializers
from django.http import HttpResponse,HttpResponseNotAllowed,JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from api.models import Product
import json



def products_view(request,*args,**kwargs):
    if request.method == 'GET':
        products = Product.objects.all().order_by('-category','-name')
        answer_list = []
        for product in products:
            answer = {}
            answer['name'] = product.name
            answer['price'] = str(product.price)
            answer['category'] = product.category
            answer_list.append(answer)
        answer_as_json = json.dumps(answer_list)
        response = HttpResponse(answer_as_json)
        response ['Content-Type'] = 'application/json'
        return response
    
@ensure_csrf_cookie
def get_token_view(request,*args,**kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET requests are allowed')

def product_view(request,pk,*args,**kwargs):
    if request.method == 'GET':
        product = [Product.objects.get(pk=pk)]
        product_data = serializers.serialize('json', product)
        response = HttpResponse(product_data)
        response['Content-type'] = 'application/json'
        return response
    
def add_product_view(request,*args,**kwargs):
    if request.method == 'POST':
        if request.body:
            product_data = serializers.deserialize('json',request.body)
            for product in product_data:
                product.save()
                return JsonResponse({'id': product.object.pk})
            else:
                response = JsonResponse({'error': 'No data provided'})
                response.status_code = 400
                return response

def delete_product_view(request,pk,*args,**kwargs):
    if request.method == 'DELETE':
        if request.GET.get("confirm") != "true":
            return JsonResponse(
                {"error": "Deletion not confirmed"},
                status=400
            )
        product = get_object_or_404(Product, id=pk)
        product.delete()
        return HttpResponse(status=204)

