from django.contrib import admin
from django.urls import path
from todo import views as todo_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',todo_views.index_view),
    path('task/',todo_views.task_page)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
