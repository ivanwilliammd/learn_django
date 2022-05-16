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
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

# from restaurants.views import home, about, contact, ContactView, AboutView, ContactView, restaurant_listview
from restaurants.views import (
    HomeView, 
    # RestaurantListView, 
    # RestaurantDetailView, 
    # restaurant_createview,
    # RestaurantCreateView,
    # logout_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    # path('accounts/logout/', logout_view, name='logout'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('restaurants/', include(('restaurants.urls', 'restaurants'), namespace='restaurants')),
    path('items/', include(('menus.urls', 'menus'), namespace='menus')),
    
    re_path(r'^$', HomeView.as_view(), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    # path('contact/', ContactView.as_view()),
    # path('contact/<int:id>/', ContactView.as_view()),
]
