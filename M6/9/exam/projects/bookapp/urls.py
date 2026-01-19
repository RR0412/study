from django.urls import path
from bookapp import views as bookapp_views

urlpatterns = [
    path('',bookapp_views.books_list,name = 'books'),
    path('add/',bookapp_views.add_book, name = 'book_add'),
    path('change/<int:pk>/',bookapp_views.change_book, name = 'book_change'),
    path('delete/<int:pk>/',bookapp_views.delete_book, name = 'book_delete')
]