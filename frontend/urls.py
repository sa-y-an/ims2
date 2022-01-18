from django.urls import path, include
from django.views.generic import TemplateView
from .  import views

app_name = "frontend"

urlpatterns = [
    path('', TemplateView.as_view(template_name =  'frontend/index.html') ),
    path("categories/", views.categoriesList , name = "categories-list" )
]
