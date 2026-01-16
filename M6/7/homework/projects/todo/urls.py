from django.urls import path
from todo import views as todo_views

urlpatterns = [
    path('index/',todo_views.index_view,name='index'),
    path('task/',todo_views.task_page,name='create_task'),
    path('success/',todo_views.success_view,name='success'),
    path('get-token/',todo_views.get_token_view),
    path('task_list/',todo_views.task_list,name='task_list'),
    path('task/<int:pk>/',todo_views.task_view, name='task_view'),
    path('tasks/',todo_views.task_list_view, name = 'task_list_api'),
    path('task/create/',todo_views.task_create_view, name = 'task_create_api'),
    path('onetask/<int:pk>/',todo_views.one_task_view, name = 'one_task_api')
]