from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    name = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField()
    type = models.TextField(default='common')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name, self.price, self.amount, self.type, self.created_date