from os import name
from django.urls import path, include
from django.views.generic import TemplateView
from .  import views


app_name = "inventory"

urlpatterns = [
    path('', TemplateView.as_view(template_name =  'inventory/index.html') , name="index"),
    path('category-list', views.categorylist)
]
