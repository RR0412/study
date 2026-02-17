from django.urls import path
from tracker import views

urlpatterns = [
    path('tasks/', views.TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view()),
]