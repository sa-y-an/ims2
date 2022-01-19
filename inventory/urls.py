from os import name
from django.urls import path, include
from django.views.generic import TemplateView
from .views  import *


app_name = "inventory"

urlpatterns = [
    path('', TemplateView.as_view(template_name =  'inventory/index.html') , name="index"),

    # category
    path('category-list', CategoryList.as_view(template_name="inventory/category-list.html"), name="cat-list"),
    path('category/add/', CategoryCreateView.as_view(template_name = "inventory/createview.html"), name='cat-add'),
    path('category/<int:pk>/', CategoryUpdateView.as_view(template_name = "inventory/createview.html"), name='cat-update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(template_name = "inventory/deleteview.html"), name='cat-delete'),

    # product
]
