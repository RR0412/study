from django.db import models

class Status(models.Model):   
    name = models.CharField(max_length=50,null=False,blank=False, verbose_name='Статус')

    def __str__(self):
        return f'{self.name}'
    

class Type(models.Model):
    name = models.CharField(max_length=50, null=False,blank=False, verbose_name='Тип')

    def __str__(self):
        return f'{self.name}'

class Task(models.Model):            
    title = models.CharField(max_length=200, null=False, blank=False,verbose_name='Заголовок')
    description = models.TextField(blank=True, verbose_name='Описание')
    status = models.ForeignKey('tracker.Status', on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    types = models.ManyToManyField('tracker.Type', related_name='tasks',blank=True)

    def __str__(self):
        return f'{self.pk}.{self.title}'


