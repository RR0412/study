from django.db import models

class Task(models.Model):
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name = 'Описание')
    status = models.CharField(max_length=200, null=False, blank=False, default= 'New', verbose_name='Статус')
    due_date = models.DateField(null=True, blank=True,verbose_name='Дата выполнения')

def __str__(self):
    return f'{self.description} - {self.status}'