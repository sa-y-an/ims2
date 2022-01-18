from pickle import TRUE
from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Categories(models.Model) :
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.title


class Attributes(models.Model) :
    value = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.value

class Brand(models.Model) :
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model) :
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to ="images/", default="images/default.png")

    # foreign keys
    category = models.ManyToManyField(Categories)
    brand = models.ForeignKey(Brand, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.title



class ProductInventory(models.Model) :

    class Variants(models.IntegerChoices) :
        pro = 3
        native = 2
        lite = 1

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    version = models.SlugField(unique=True, max_length=100)
    # attributes
    customAttribute = models.ForeignKey(Attributes, on_delete=models.RESTRICT, blank=True, null=True)
    variant = models.IntegerField(choices=Variants.choices, default=2)   

    # prices
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.version


class Stock(models.Model) :
    stock = models.IntegerField()
    sold = models.IntegerField()
    debit = models.DateTimeField(default=datetime.utcnow()+timedelta(hours=5.5))
    credit = models.DateTimeField(default=datetime.utcnow()+timedelta(hours=5.5))
    inventory = models.OneToOneField(ProductInventory, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.inventory.version + "," + str(self.stock) + "," + str(self.sold)

