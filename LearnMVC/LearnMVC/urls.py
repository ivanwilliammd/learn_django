"""LearnMVC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView

# from restaurants.views import home, about, contact, ContactView, AboutView, ContactView, restaurant_listview
from restaurants.views import HomeView, RestaurantListView, RestaurantDetailView, restaurant_createview

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', HomeView.as_view(), name='home'),
    path('restaurants/', RestaurantListView.as_view()),
    path('restaurants/create', restaurant_createview),
    path('restaurants/category/<category>/', RestaurantListView.as_view()),
    # path('restaurants/<pk>/', RestaurantDetailView.as_view()),
    # path('restaurants/<rest_id>/', RestaurantDetailView.as_view()),
    re_path(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view()),
    path('about/', TemplateView.as_view(template_name='about.html')),
    path('contact/', TemplateView.as_view(template_name='contact.html')),
    # path('contact/', ContactView.as_view()),
    # path('contact/<int:id>/', ContactView.as_view()),
]
