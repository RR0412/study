from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from book.models import Book
from book.serializers import BookSerializer

class BookListCreateView(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class BookReadUpdateDeleteView(APIView):
    def dispatch(self,request, *args, **kwargs):
        self.book=get_object_or_404(Book, id=kwargs.get('id'))
        return super().dispatch(request, *args , **kwargs)
    
    def get(self, request, *args, **kwargs):
        serializer = BookSerializer(self.book)
        return Response(serializer.data)
    
    def patch(self, request, *args, **kwargs):
        serializer = BookSerializer(self.book)
        serializer.update(self.book, request.data)
        return Response(serializer.data)
    
    def delete(self, request, *args, **kwargs):
        self.book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



