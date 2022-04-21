from datetime import datetime
from django.db import models
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from shop.models import Product, Customer

class Command(BaseCommand):
    help = 'Load data into the tables'

    def handle(self, *args, **options):
        User.objects.create_user(username='Zhaoqi.C', password='123', email='543315720@qq.com').save()
        Customer.objects.create(username='Zhaoqi.C', email='543315720@qq.com', balance=10000).save()


