from django.shortcuts import render
from inventory.models import Categories
from django.db.models import Count

# Create your views here.
def categories(request) :
    data = Categories.objects.all().annotate(
    product_count=Count('product'))
    
    return render(request, "frontend/categories.html", {"data": data})
