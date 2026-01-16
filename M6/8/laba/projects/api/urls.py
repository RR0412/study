from django.urls import path
from api import views as api_views

urlpatterns = [
    path('task_list/',api_views.task_list_view,name = 'task_list'),
    path('task/<int:pk>/',api_views.task_view, name = 'task')
]