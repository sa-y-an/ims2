from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


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

class CategoryUpdateView(UpdateView):
    model = Categories
    fields = '__all__'
    success_url = reverse_lazy('inventory:cat-list')

class CategoryDeleteView(DeleteView):
    model = Categories
    success_url = reverse_lazy('inventory:cat-list')


# brand


class BrandList(ListView) :
    model = Brand


class BrandCreateView(CreateView):
    model = Brand
    fields = '__all__'
    success_url = reverse_lazy('inventory:brand-list')

class BrandCreateView(CreateView):
    model = Brand
    fields = '__all__'
    success_url = reverse_lazy('inventory:brand-list')


class BrandUpdateView(UpdateView):
    model = Brand
    fields = '__all__'
    success_url = reverse_lazy('inventory:brand-list')

class BrandDeleteView(DeleteView):
    model = Brand
    success_url = reverse_lazy('inventory:brand-list')


# Attribute


class AtbList(ListView) :
    model = Attributes


class AtbCreateView(CreateView):
    model = Attributes
    fields = '__all__'
    success_url = reverse_lazy('inventory:atb-list')

class AtbCreateView(CreateView):
    model = Attributes
    fields = '__all__'
    success_url = reverse_lazy('inventory:atb-list')


class AtbUpdateView(UpdateView):
    model = Attributes
    fields = '__all__'
    success_url = reverse_lazy('inventory:atb-list')

class AtbDeleteView(DeleteView):
    model = Attributes
    success_url = reverse_lazy('inventory:atb-list')


# products (prod)


class ProdList(ListView) :
    model = Product


class ProdCreateView(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('inventory:prod-list')

class ProdCreateView(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('inventory:prod-list')


class ProdUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('inventory:prod-list')

class ProdDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('inventory:prod-list')

