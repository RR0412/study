from django.shortcuts import render

def index_view(request):
    return render(request,'index.html')

def hello_view(request):
    return render(request,'hello.html')