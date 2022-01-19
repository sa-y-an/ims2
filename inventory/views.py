from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


# Create your views here.

# category views 

class CategoryList(ListView) :
    model = Categories


class CategoryCreateView(CreateView):
    model = Categories
    fields = '__all__'
    success_url = reverse_lazy('inventory:cat-list')

class CategoryCreateView(CreateView):
    model = Categories
    fields = '__all__'
    success_url = reverse_lazy('inventory:cat-list')


class PostCreateView(CreateView):
    model = Product
    fields = []

class CategoryUpdateView(UpdateView):
    model = Categories
    fields = '__all__'
    success_url = reverse_lazy('inventory:cat-list')

class CategoryDeleteView(DeleteView):
    model = Categories
    success_url = reverse_lazy('inventory:cat-list')
