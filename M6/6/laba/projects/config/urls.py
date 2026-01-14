from django.contrib import admin
from django.urls import path
from shop import views as shop_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',shop_views.index,name='index'),
    path('products/',shop_views.products_view,name='products'),
    path('products/<int:pk>/',shop_views.product_view,name='product'),
    path('categories/add',shop_views.category_add_view,name='add_category'),
    path('products/add',shop_views.product_add_view,name='add_product'),
    path('categories/',shop_views.categories_view,name='categories'),
    path('categories/<int:pk>/delete/',shop_views.category_delete_view,name='category_delete'),
    path('categories/<int:pk>/edit/',shop_views.category_edit_view,name='category_edit'),
    path('products/<int:pk>/delete/',shop_views.product_delete_view,name='product_delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
