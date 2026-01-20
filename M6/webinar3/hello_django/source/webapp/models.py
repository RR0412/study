from django.db import models

class Article(models.Model):
    class StatusChoices(models.TextChoices):
        active = 'active','Активна'
        in_progres = 'in_progress', 'В процессе обработки'
        inactive ='inactive',  'Неактивна'

    title = models.CharField(max_length=200, null=False, blank=False,verbose_name='Заголовок')
    text = models.TextField(max_length=3000, null=False, blank=False,verbose_name='Текст')
    author = models.CharField(max_length=40, null=False, blank=False,default='Unknown',verbose_name='Автор')   
    status = models.CharField(max_length=50, choices= StatusChoices.choices)   
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')


    def __str__(self):
        return f'{self.pk}. {self.title}'