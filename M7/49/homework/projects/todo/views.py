from django.shortcuts import render, get_object_or_404
from todo.models import Task
from rest_framework.views import APIView
from rest_framework.response import Response

class TaskListCreateView(APIView):
    def post(self,request):
        description = request.data.get('description')
        details = request.data.get('details') or None
        status = request.data.get('status')
        due_date = request.data.get('due_date') or None

        if not description or not status:
            return Response ({'error': 'All field are required.'},
status=status.HTTP_400_BAD_REQUEST)
        
        task = Task.objects.create(
            description = description,
            details = details or None,
            status = status,
            due_date = due_date or None
        )
        
        return Response({
            'id': task.id,
            'description': task.description,
            'details': task.details or None,
            'status': task.status,
            'due_date': task.due_date or None
        })
    
    def get(self,request):
        tasks = Task.objects.all()
        answer=[]
        for task in tasks:
            answer.append({
            'id': task.id,
            'description': task.description,
            'details':task.details or None,
            'status':task.status,
            'due_date':task.due_date or None
            })            
        return Response(answer)



class TaskDetailView(APIView):
    def get(self, request, id):
        task = get_object_or_404(Task, id=id)

        return Response({
            'id': task.id,
            'description': task.description,
            'details':task.details or None,
            'status':task.status,
            'due_date':task.due_date or None
        })
