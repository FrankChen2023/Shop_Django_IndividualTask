import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError
import random
from shop.models import Product, Customer

class Command(BaseCommand):
    help = 'Load data into the tables'

    def handle(self, *args, **options):
        
        Product.objects.filter(name='').delete()
        Product.objects.filter(price=0.00).delete()
                
        print("data parsed successfully")


