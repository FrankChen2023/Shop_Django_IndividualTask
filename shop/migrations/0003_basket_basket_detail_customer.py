# Generated by Django 4.0.4 on 2022-04-15 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('basketname', models.TextField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Basket_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('username', models.TextField()),
                ('basketname', models.TextField()),
                ('address', models.TextField()),
                ('item', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('username', models.TextField()),
                ('email', models.TextField()),
                ('balance', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
