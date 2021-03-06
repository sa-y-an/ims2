from curses.panel import version
from unicodedata import category
from django.shortcuts import render
from inventory.models import Categories, Product, ProductInventory
from django.db.models import Count
from django.shortcuts import get_object_or_404

# Create your views here.
def categoriesList(request) :
    data = Categories.objects.all().annotate(
    product_count=Count('product'))

    return render(request, "frontend/categories.html", {"data": data})

def productPage(request, slug) :
    data = Product.objects.filter(category__slug = slug)
    catData = get_object_or_404(Categories , slug = slug)
    return render(request,"frontend/catprods.html",{"data":data,"catData":catData})

def inventories(request,slug) :
    data = ProductInventory.objects.filter(product__slug = slug)
    return render(request, "frontend/inventories.html",{"data":data})

def listProduct(request):
    data = Product.objects.all()
    return render(request,"frontend/catprods.html",{"data":data})

def inventory(request,slug) :
    data = get_object_or_404(ProductInventory,version=slug)
    # print(data.product.slug)
    categories = Categories.objects.filter(product__slug = data.product.slug)
    return render(request,"frontend/inventory.html", {"data":data, "categories":categories})