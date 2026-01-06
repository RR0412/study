from django.contrib import admin
from django.urls import path
from calculatorapp import views as calculatorapp_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',calculatorapp_views.index_view),
    path('form/',calculatorapp_views.calculate)
] + static(settings.MEDIA_URL, document_root=settings.
           MEDIA_ROOT)
