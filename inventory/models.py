from distutils.command.upload import upload
from email.policy import default
from turtle import title
from unicodedata import category
import uuid
from django.db import models
from datetime import datetime, timedelta


from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# Create your models here.
class Categories(models.Model) :
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.title


class Attributes(models.Model) :
    type = models.CharField(max_length=100, unique=True)
    value = models.IntegerChoices()
    description = models.CharField(max_length=155)

    def __str__(self) -> str:
        return self.type

class Brand(models.Model) :
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model) :
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload="images/", default="images/default.png")

    # foreign keys
    category = models.ManyToManyField(Categories, on_delete=models.RESTRICT)
    brand = models.ForeignKey(Brand, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.title


class Stock(models.Model) :
    stock = models.IntegerField()
    sold = models.IntegerField()
    debit = models.DateTimeField(default=datetime.utcnow()+timedelta(hours=5.5))
    credit = models.DateTimeField(default=datetime.utcnow()+timedelta(hours=5.5))


class ProductInventory(models.Model) :
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    uuid = models.UUIDField(unique=True)
    attributes = models.ManyToManyField(blank=True, null=True)
    price = models.IntegerField()
    stock = models.OneToOneField(Stock, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.uuid