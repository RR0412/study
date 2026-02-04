from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from tracker.models import Task
from tracker.serializers import TaskSerializer

class TaskListCreateView(APIView):
    def get(self,request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = serializer.save()
        response_data = TaskSerializer(task).data
        return Response(response_data,
                        status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskReadUpdateDeleteView(APIView):
    def dispatch(self,request,*args,**kwargs):
        self.task=get_object_or_404(Task, id=kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get_task_response(self):
        serializer = TaskSerializer(instance=self.task)
        return Response(serializer.data)
    
    def get(self, request, *args, **kwargs):
        return self.get_task_response()
    
    def patch(self, request, *args, **kwargs):
        for key,value in request.data.items():
            setattr(self.task, key, value)

        self.task.save()
        return self.get_task_response()
    
    def delete(self, request, *args, **kwargs):
        self.task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)