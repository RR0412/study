from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, null = False, blank=False, verbose_name = 'Название категории')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name = 'Описание категории')


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name = 'Название товара')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name = 'Описание товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    image = models.URLField(max_length=300, null=True, blank=True, verbose_name='ССылка на изображение')

    def __str__(self):
        return f'{self.name} - {self.price}'
    


