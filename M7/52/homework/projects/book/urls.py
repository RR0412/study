from django.urls import path
from book import views

urlpatterns = [
    path('api/books/', views.BookListCreateView.as_view()),
    path('api/books/<id>/',views.BookReadUpdateDeleteView.as_view()),
]