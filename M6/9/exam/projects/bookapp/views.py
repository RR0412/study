from django.shortcuts import render, redirect, get_object_or_404
from bookapp.models import Book

def books_list(request):   
    sorted_books = Book.objects.all().order_by('-created_at')
    books = sorted_books.filter(status='active')
    return render(request, 'bookapp/books_list.html', {'books' : books})

def add_book(request):
    if request.method == 'GET':
        return render(request, 'bookapp/book_add.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('text')
        Book.objects.create(name=name,email=email,text=text)
        return redirect('books')


def change_book(request,pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('text')
        book = Book.objects.create(name=name,email=email,text=text)
        book.save()
        return redirect('books')
    return render(request, 'bookapp/book_change.html',{'book': book})

def delete_book(request,pk):
    book=get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('books')
    return render (request,'bookapp/book_confirm_delete.html',{'book': book})
