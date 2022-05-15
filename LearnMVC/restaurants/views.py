from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
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


# def restaurant_listview(request):
#     template_name = 'restaurants/restaurant_list.html'
#     queryset = RestaurantLocation.objects.all()
#     context = {
#         "restaurants" : queryset,
#         "title" : 'Restaurants | IvanMD',
#     }
#     return render(request, template_name, context)

# def restaurant_detailview(request, slug):
#     template_name = 'restaurants/restaurantlocation_detail.html'
#     obj = RestaurantLocation.objects.get(slug=slug)
#     context = {
#         "object":obj
#     }
#     return render(request, template_name, context)


class RestaurantListView(ListView):

    def get_queryset(self):
        print(self.kwargs)
        category = self.kwargs.get('category')
        if category:
            queryset =  RestaurantLocation.objects.filter(
                Q(category__iexact=category) |
                Q(category__icontains=category)
                )
        else :
            queryset = RestaurantLocation.objects.all()
        return queryset

class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

    # def get_context_data(self, *args, **kwargs):
    #     print(self.kwargs)
    #     context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(RestaurantLocation, id=rest_id) #pk = rest_id
    #     return obj

# # Function based view.
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