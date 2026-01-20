from django.urls import path
from bookapp import views as bookapp_views

urlpatterns = [
    path('',bookapp_views.books_list,name = 'books'),
    path('add/',bookapp_views.add_book, name = 'book_add'),
    path('change/<int:pk>/',bookapp_views.change_book, name = 'book_change'),
    path('delete/<int:pk>/',bookapp_views.delete_book, name = 'book_delete'),
    path('api/books/',bookapp_views.book_view, name = 'api_books'),
    path('api/books/<int:pk>/',bookapp_views.book_detail_view, name = 'api_book_CRUD')
]