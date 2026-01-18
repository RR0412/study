from django.db import models
STATUS_CHOICES = [
    ('active','Активно'),
    ('blocked','Заблокировано'),
]
class Book(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name = 'Имя')
    email = models.EmailField(max_length=100, null=False, blank=False, verbose_name = 'Электронная почта')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name = 'Текст записи')
    created_at = models.DateTimeField(auto_now_add=True)
    last_changed_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length = 20, null=False, blank=False, choices = STATUS_CHOICES, default = 'active')

    def __str__(self):
        return f'{self.name} - {self.status}'