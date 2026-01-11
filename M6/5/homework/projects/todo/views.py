from django.shortcuts import render, get_object_or_404
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
        task.details = request.POST.get('details')
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

def task_view(request,pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_view.html', context={'task': task})

