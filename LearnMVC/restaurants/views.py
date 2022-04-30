from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
import random

from .models import RestaurantLocation

# Template View
class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        print(context)
        context = {
            "title" : "IvanMD",
            "section" : "Home",
            "num" : random.randint(1,100),
            "some_list" : [random.randint(1,10000), random.randint(1,1000), random.randint(1,100000)]
        }
        return context


# def restaurant_listview
# def restaurant_listview(request):
#     template_name = 'restaurants/restaurant_list.html'
#     queryset = RestaurantLocation.objects.all()
#     context = {
#         "restaurants" : queryset,
#         "title" : 'Restaurants | IvanMD',
#     }
#     return render(request, template_name, context)


class RestaurantListView(ListView):
    queryset = RestaurantLocation.objects.all()
    
class SearchRestaurantListView(ListView):
    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs.get('slug')
        if slug:
            queryset =  RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
                )
        else :
            queryset = RestaurantLocation.objects.none()
        return queryset

# # Fucntion based view.
# def home(request):
#     context = {
#                 "title" : "IvanMD",
#                 "section" : "Home",
#                 "num" : random.randint(1,100),
#                 "some_list" : [random.randint(1,10000), random.randint(1,1000), random.randint(1,100000)]
#             }
#     return render(request, 'home.html', context)
#     # return HttpResponse('Hello, World!')

# def about(request):
#     context = {
#                 "title" : "IvanMD",
#                 "section" : "About",
#             }
#     return render(request, 'about.html', context)

# def contact(request):
#     context = {
#                 "title" : "IvanMD",
#                 "section" : "Contact",
#             }
#     return render(request, 'contact.html', context)

# # Classic Based View
# class ContactView(View):
#     def get(self, request, *args, **kwargs):
#         context = {}
#         return render(request, 'contact.html', context)

# # Template View
# class AboutView(TemplateView):
#     template_name = 'about.html'

# class ContactView(TemplateView):
#     template_name = 'contact.html'