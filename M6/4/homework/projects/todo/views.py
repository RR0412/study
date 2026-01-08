from django.shortcuts import render

def index_view(request):
    return render(request, 'todo/index.html')

def task_page(request):
    if request.method == 'GET':
        return render(request,'todo/form.html')
