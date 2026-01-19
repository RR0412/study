from django.urls import path
from bookapp import views as bookapp_views

urlpatterns = [
    path('',bookapp_views.books_list,name = 'books'),
    path('add/',bookapp_views.add_book, name = 'book_add'),
]