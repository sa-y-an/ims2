from django.contrib import admin
from .models import Categories, Product, ProductInventory, Brand, Attributes

# Register your models here.
admin.site.register(Categories)
admin.site.register(Product)
admin.site.register(ProductInventory)
admin.site.register(Brand)
admin.site.register(Attributes)
