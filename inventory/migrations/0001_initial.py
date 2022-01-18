# Generated by Django 4.0.1 on 2022-01-18 04:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(max_length=255)),
                ('image', models.ImageField(default='images/default.png', upload_to='images/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory.brand')),
                ('category', models.ManyToManyField(to='inventory.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.SlugField(max_length=100, unique=True)),
                ('price', models.IntegerField()),
                ('attributes', models.ManyToManyField(blank=True, to='inventory.Attributes')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField()),
                ('sold', models.IntegerField()),
                ('debit', models.DateTimeField(default=datetime.datetime(2022, 1, 18, 9, 46, 23, 645466))),
                ('credit', models.DateTimeField(default=datetime.datetime(2022, 1, 18, 9, 46, 23, 645489))),
                ('inventory', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.productinventory')),
            ],
        ),
    ]
