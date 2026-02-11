from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from tracker.models import Task
from tracker.serializers import TaskSerializer,TaskReadSerializer

class TaskListCreateView(APIView):
    def get(self,request):
        tasks = Task.objects.all()
        serializer = TaskReadSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
    
class TaskReadUpdateDeleteView(APIView):
    def dispatch(self,request,*args,**kwargs):
        self.task=get_object_or_404(Task, id=kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        serializer = TaskReadSerializer(self.task)
        return Response(serializer.data)
    
    def patch(self, request, *args, **kwargs):
        serializer = TaskSerializer(self.task)
        serializer.update(self.task, request.data)
        return Response(serializer.data)
    
    def delete(self, request, *args, **kwargs):
        self.task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)