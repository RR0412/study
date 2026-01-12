from django.contrib import admin
from django.urls import path
from shop import views as shop_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',shop_views.products_view),
    path('products/',shop_views.products_view),
    path('products/<int:pk>/',shop_views.product_view),
    path('categories/add',shop_views.category_add_view),
    path('products/add',shop_views.product_add_view)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
