from django.urls import path
from api import views as api_views

urlpatterns = [
    path('products/',api_views.products_view,name = 'products'),
    path('token/',api_views.get_token_view,name = 'token'),
    path('product/<int:pk>/',api_views.product_view, name = 'product')
]

# X-CSRFToken

# fWqrmpouGlSuaoZ6peCkcDUMJImSBW1j