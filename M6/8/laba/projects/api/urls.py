from django.urls import path
from api import views as api_views

urlpatterns = [
    path('products/',api_views.products_view,name = 'products'),
    path('token/',api_views.get_token_view,name = 'token'),
    path('product/<int:pk>/',api_views.product_view, name = 'product'),
    path('product/add/',api_views.add_product_view, name = 'product_add'),
    path('product/delete/<int:pk>/',api_views.delete_product_view, name = 'product_delete')
]

