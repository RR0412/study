from rest_framework import serializers
from tracker.models import Task
from tracker.models import Status
from tracker.models import Type

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_blank=True)
    status = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all())
    type = serializers.PrimaryKeyRelatedField(queryset=Type.objects.all())
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
