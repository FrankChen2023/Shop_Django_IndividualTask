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
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/shop/data.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            type = 'common'
            for row in reader:
                print(row)
                amount = random.randrange(20,999)
                try:
                    Product.objects.create(name=row[0], type=type, amount=amount, price=row[1]).save()
                except:
                    pass
                
        print("data parsed successfully")


