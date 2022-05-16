from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import ItemForm
from .models import Item
# Create your views here.


class ItemListView(ListView):

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemDetailView(DetailView):

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class ItemCreateView(CreateView):

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    form_class = ItemForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(ItemCreateView, self).form_valid(form)


class ItemUpdateView(UpdateView):

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    form_class = ItemForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(ItemUpdateView, self).form_valid(form)