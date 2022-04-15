# Generated by Django 4.0.4 on 2022-04-15 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_customer_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='total_price',
        ),
        migrations.AddField(
            model_name='basket',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='basket',
            name='name',
            field=models.TextField(default=''),
        ),
    ]
