from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
import random

from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
from .models import RestaurantLocation
from django.contrib.auth import logout


# @login_required
# # Logout Request
# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect("/")

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

# @login_required
# def restaurant_createview(request):
#     # form = RestaurantCreateForm(request.POST or None)
#     form = RestaurantLocationCreateForm(request.POST or None)
#     errors = None
#     if form.is_valid() and request.user.is_authenticated():
#         instance = form.save(commit=False)
#         instance.owner = request.user
#         instance.save()
#         # obj = RestaurantLocation.objects.create(
#         #         name = form.cleaned_data.get('name'),
#         #         location = form.cleaned_data.get('location'),
#         #         category = form.cleaned_data.get('category'),
#         #         # name = name,
#         #         # location = location,
#         #         # category = category
#         #     )
#         return HttpResponseRedirect("/restaurants")
#     if form.errors:
#         errors = form.errors

#     template_name = 'restaurants/forms.html'
#     context = {"form": form, "errors": errors}
#     return render(request, template_name, context)

class RestaurantListView(LoginRequiredMixin, ListView):

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

class RestaurantDetailView(LoginRequiredMixin, DetailView):
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

class RestaurantCreateView(LoginRequiredMixin, CreateView):
    # login_url = '/login/'
    form_class = RestaurantLocationCreateForm
    template_name = 'forms.html'
    # success_url = "/restaurants/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context

class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'restaurants/detail-update.html'

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)
        # return RestaurantLocation.objects.all()

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantUpdateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        context['title'] = f'Update {name}'
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