from django.shortcuts import render, get_object_or_404, redirect
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
        description = request.POST.get('description')
        details = request.POST.get('details')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')
        if due_date:
            due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        else:
            due_date = None
        task = Task.objects.create(description=description, details=details, status=status, due_date=due_date )
        return redirect('task_view', pk=task.pk)

def task_list(request):
    tasks=Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def task_view(request,pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todo/task_view.html', context={'task': task})

