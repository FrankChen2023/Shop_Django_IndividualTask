from datetime import datetime
from django.db import models
from django.core.management.base import BaseCommand, CommandError

from shop.models import Product

class Command(BaseCommand):
    help = 'Load data into the tables'

    def handle(self, *args, **options):

        Product.objects.create(name='Apple', price=1.99, amount=999, type='Food').save()
        Product.objects.create(name='Banana', price=2.63, amount=999, type='Food').save()
        Product.objects.create(name='Orange', price=1.40, amount=999, type='Food').save()
        Product.objects.create(name='Adidas T-shirt', price=27.48, amount=20, type='Clothes').save()
        Product.objects.create(name='Nike Air Max 2090', price=109.99, amount=20, type='Clothes').save()
        Product.objects.create(name='Supreme Shorts', price=89.99, amount=20, type='Clothes').save()
        Product.objects.create(name='Bed Sheet', price=14.85, amount=100, type='Living').save()
        Product.objects.create(name='Towel', price=9.08, amount=100, type='Living').save()
        Product.objects.create(name='Electric Toothbrush', price=64.99, amount=100, type='Living').save()
        Product.objects.create(name='Mountain Bike', price=219.99, amount=50, type='Activities').save()
        Product.objects.create(name='Travel Umbrella', price=15.99, amount=200, type='Activities').save()
        Product.objects.create(name='Basketball', price=33.70, amount=200, type='Activities').save()
        Product.objects.create(name='Apple iphone 13 Pro Max', price=1149.00, amount=20, type='Common').save()