from django.db import models
CATEGORY_CHOICES = [
    ('food', 'food'),
    ('furniture', 'furniture'),
    ('clothes', 'clothes'),
    ('electronics', 'electronics'),
    ('pets', 'pets'),
]

class Product(models.Model):
    name = models.CharField(max_length = 100, null=False, blank=False)
    description = models.TextField(max_length = 2000, null=True, blank=True)
    category = models.CharField(max_length = 20,null=False, blank=False, choices = CATEGORY_CHOICES, default = 'other')
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=7,decimal_places=2)

    def __str__(self):
        return f'{self.name}-{self.category}'
    
