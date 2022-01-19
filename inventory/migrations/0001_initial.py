# Generated by Django 4.0.1 on 2022-01-19 18:00

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
                ('variant', models.IntegerField(choices=[(3, 'Pro'), (2, 'Native'), (1, 'Lite')], default=2)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField(default=0)),
                ('sold', models.IntegerField(default=0)),
                ('debitDate', models.DateTimeField(default=datetime.datetime(2022, 1, 19, 23, 30, 8, 421763), help_text='format: required, YYYY-MM-DD HH:MN:SC (2022-01-19 17:29:19) ')),
                ('creditDate', models.DateTimeField(default=datetime.datetime(2022, 1, 19, 23, 30, 8, 421785), help_text='format: required, YYYY-MM-DD HH:MN:SC (2022-01-19 17:29:19) ')),
                ('customAttribute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='inventory.attributes')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
    ]