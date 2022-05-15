from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from .views import (
    HomeView, 
    RestaurantListView, 
    RestaurantDetailView, 
    # restaurant_createview,
    RestaurantCreateView,
)

urlpatterns = [
    path('', RestaurantListView.as_view(), name='restaurants'),
    path('create', RestaurantCreateView.as_view(), name='restaurants-create'),
    path('category/<category>/', RestaurantListView.as_view()),
    re_path(r'(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='restaurant-detail'),

    # path('restaurants/<pk>/', RestaurantDetailView.as_view()),
    # path('restaurants/<rest_id>/', RestaurantDetailView.as_view()),

]
