from rest_framework import serializers
from tracker.models import Task
from tracker.models import Status
from tracker.models import Type


class StatusNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'name')


class TypeNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'name')

class TaskReadSerializer(serializers.ModelSerializer):
    status = StatusNestedSerializer(read_only=True)
    type = TypeNestedSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'status', 'type', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class TaskSerializer(serializers.ModelSerializer):
    status = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all())
    type = serializers.PrimaryKeyRelatedField(queryset=Type.objects.all())

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'status', 'type', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')



