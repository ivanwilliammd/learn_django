from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from .views import (
    ItemCreateView,
    ItemListView,
    ItemDetailView,
    ItemUpdateView,
)

urlpatterns = [
    path('', ItemListView.as_view(), name='list'),
    path('create', ItemCreateView.as_view(), name='create'),
    re_path(r'(?P<pk>[\w-]+)/$', ItemDetailView.as_view(), name='detail'),

    # path('restaurants/<pk>/', RestaurantDetailView.as_view()),
    # path('restaurants/<rest_id>/', RestaurantDetailView.as_view()),

]
