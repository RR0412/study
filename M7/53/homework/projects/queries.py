from tracker.models import Task,Status,Type
from datetime import timedelta,datetime
from django.db.models import Q

##1
month_ago = datetime.now() - timedelta(days=30)
Task.objects.filter(status_id=3, updated_at__gte=month_ago)

##2
new=Status.objects.get(name='New')
done=Status.objects.get(name='Done')
task=Type.objects.get(name='Task')
bug=Type.objects.get(name='Bug')
tasks = Task.objects.filter((Q(status=new)| Q(status=done)) & (Q(type=task) | Q(type=bug)))

##3
bug=Type.objects.get(name='Bug')
done=Status.objects.get(name='Done')
task = Task.objects.filter((Q(title__icontains="bug")) & Q(type=bug) & ~ Q (status=done))


##4
Task.objects.values('id', 'title', 'status__name', 'type__name')
