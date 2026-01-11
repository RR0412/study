from django.contrib import admin
from django.urls import path
from todo import views as todo_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',todo_views.index_view,name='index'),
    path('task/',todo_views.task_page,name='create_task'),
    path('success/',todo_views.success_view,name='success'),
    path('task_list/',todo_views.task_list,name='task_list'),
    path('task/<int:pk>',todo_views.task_view, name='task_view'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
