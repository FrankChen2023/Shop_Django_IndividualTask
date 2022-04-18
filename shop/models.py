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

class Customer(models.Model):
    username = models.TextField()
    email = models.TextField()
    balance = models.DecimalField(max_digits=8, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username, self.email, self.balance, self.created_date

class Basket(models.Model):
    username = models.TextField()
    basketname = models.TextField()
    name = models.TextField(default='')
    address = models.TextField(default='')
    status = models.TextField(default='unpaid')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username, self.basketname, self.name, self.address, self.created_date

class Basket_Detail(models.Model):
    name = models.TextField()
    username = models.TextField()
    basketname = models.TextField()
    address = models.TextField()
    item = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name, self.username, self.basketname, self.address, 
        self.item, self.price, self.total_price, self.amount, self.created_date

