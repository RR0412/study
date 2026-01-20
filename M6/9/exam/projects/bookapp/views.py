from django.shortcuts import render, redirect, get_object_or_404
from bookapp.models import Book
from  django.http import HttpResponse,HttpResponseNotAllowed,JsonResponse
import json
from django.views.decorators.csrf import ensure_csrf_cookie

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
        name = request.POST.get('name')asd
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


def book_view(request,*args,**kwargs):
    if request.method == 'GET':
        books = Book.objects.all()
        answer_list = []
        for book in books:
            answer = {
            'name' : book.name,
            'email': book.email,
            'text' : book.text
            }
            answer_list.append(answer)
        return JsonResponse(answer_list, safe=False)
    elif request.method == 'POST':
        try:
            book_data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        book = book.objects.create(
            name=book_data['name'],
            email=book_data['email'],
            text=book_data['text'],
        )
        return JsonResponse({"id": book.pk}, status=201)
        
    
@ensure_csrf_cookie
def get_token_view(request,*args,**kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])


def book_detail_view(request,pk,*args,**kwargs):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'PUT':
        book_data = json.loads(request.body)
        name = book_data['name']
        email = book_data['email'] or None
        text = book_data['text']
        book.save()
        return HttpResponse(status=204)
    
    elif request.method == 'PATCH':
        book_data = json.loads(request.body)
        for key, value in book_data.items():            
            setattr(book, key, value)
        book.save()
        return HttpResponse(status=204)

    elif request.method == 'DELETE':
        if request.GET.get("confirm") != "true":
            return JsonResponse(
                {"error": "Deletion not confirmed"},
                status=400
            )
        book.delete()
        return HttpResponse(status=204)
    
    return JsonResponse({"error": "Method not allowed"}, status = 405)