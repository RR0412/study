from django.contrib import admin
from django.urls import path
from shop import views as shop_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',shop_views.index)
] + static(settings.MEDIA_URL, documnet_root=settings.MEDIA_ROOT)
