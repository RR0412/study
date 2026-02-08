from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Наименование')
    author = models.CharField(max_length=200, verbose_name='Автор')
    published_date = models.DateTimeField(auto_now_add=True)