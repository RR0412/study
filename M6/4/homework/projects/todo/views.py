from django.shortcuts import render
from todo.models import Task
from datetime import datetime

def index_view(request):
    return render(request, 'todo/index.html')

def success_view(request):
    return render(request,'todo/success.html')

def task_page(request):
    if request.method == 'GET':
        return render(request,'todo/form.html')
    elif request.method == 'POST':
        task = Task()       
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        due_date = request.POST.get('due_date')
        if due_date:
            task.due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        else:
            task.due_date = None
        
        task.save()
        return render(request,'todo/success.html')
    
def task_list(request):
    tasks=Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

    