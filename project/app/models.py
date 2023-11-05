from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=64,verbose_name='Название продукта')
    price = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='Цена продукта')
    
    def __str__(self):
        return self.name