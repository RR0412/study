from django.shortcuts import render, get_object_or_404, redirect
from todo.models import Task
from django.core import serializers
from datetime import datetime
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse,HttpResponseNotAllowed,JsonResponse
import json


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

@ensure_csrf_cookie
def get_token_view(request,*args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')

def task_list_view(request, *args, **kwargs):
    if request.method == 'GET':
        tasks = Task.objects.all()
        tasks_data = serializers.serialize('json', tasks)
        response = HttpResponse(tasks_data)
        response ['Content-Type'] = 'application/json'
        return response
    
def task_create_view(request, *args,**kwargs):
    if request.method == 'POST':
        if request.body :
            task_data = serializers.deserialize('json',request.body)
            for task in task_data:
                task.save()
                return JsonResponse({'id': task.object.pk})
            else:
                response = JsonResponse({'error': 'No data provided'})
                response.status_code = 400
                return response


def one_task_view(request,pk,*args,**kwargs):
    if request.method == 'GET':
        task = [Task.objects.get(pk=pk)]
        task_data = serializers.serialize('json', task)
        response = HttpResponse(task_data)
        response['Content-type'] = 'application/json'
        return response
