from os import name
from django.urls import path, include
from django.views.generic import TemplateView
from .  import views


app_name = "frontend"

urlpatterns = [
    path('', TemplateView.as_view(template_name =  'frontend/index.html') , name="home"),
    path("categories/", views.categoriesList , name = "categories-list" ),

    path("product/<str:slug>", views.productPage, name="productPage"),
    path("inventories/<str:slug>", views.inventories, name="inventories"),


    path("product/", views.listProduct, name="list-products"),
    path("product/version/<str:slug>", views.inventory, name="inventory"),
]
