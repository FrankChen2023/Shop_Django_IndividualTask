from datetime import datetime
from django.db import models
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from shop.models import Product, Customer

class Command(BaseCommand):
    help = 'Load data into the tables'

    def handle(self, *args, **options):
        Customer.objects.create(username='Frank.C', email='123@123.com', balance=10000).save()


