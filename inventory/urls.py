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

    # brand

    path('brand-list', BrandList.as_view(template_name="inventory/brand-list.html"), name="brand-list"),
    path('brand/add/', BrandCreateView.as_view(template_name = "inventory/createview.html"), name='brand-add'),
    path('brand/<int:pk>/', BrandUpdateView.as_view(template_name = "inventory/createview.html"), name='brand-update'),
    path('brand/<int:pk>/delete/', BrandDeleteView.as_view(template_name = "inventory/deleteview.html"), name='brand-delete'),

    # attribute (atb)

    path('atb-list', AtbList.as_view(template_name="inventory/atb-list.html"), name="atb-list"),
    path('atb/add/', AtbCreateView.as_view(template_name = "inventory/createview.html"), name='atb-add'),
    path('atb/<int:pk>/', AtbUpdateView.as_view(template_name = "inventory/createview.html"), name='atb-update'),
    path('atb/<int:pk>/delete/', AtbDeleteView.as_view(template_name = "inventory/deleteview.html"), name='atb-delete'),

    # products 

    path('prod-list', ProdList.as_view(template_name="inventory/prod-list.html"), name="prod-list"),
    path('prod/add/', ProdCreateView.as_view(template_name = "inventory/createview.html"), name='prod-add'),
    path('prod/<int:pk>/', ProdUpdateView.as_view(template_name = "inventory/createview.html"), name='prod-update'),
    path('prod/<int:pk>/delete/', ProdDeleteView.as_view(template_name = "inventory/deleteview.html"), name='prod-delete'),

]
