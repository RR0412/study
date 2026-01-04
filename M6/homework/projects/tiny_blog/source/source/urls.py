
from django.contrib import admin
from django.urls import path
from webapp import views as webapp_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', webapp_views.index_view),
    path('2',webapp_views.hello_view),
]

