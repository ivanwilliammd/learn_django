from cProfile import Profile
from re import U
from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


from restaurants.models import RestaurantLocation
# Create your views here.

User = get_user_model()

class ProfileDetailView(DetailView):
    # queryset = User.objects.filter(is_active=True)
    template_name = 'profiles/user.html'

    def get_object(self) :
        username = self.kwargs.get("username")
        if username is None :
            raise Http404
        return get_object_or_404(User, username__iexact = username, is_active = True)

    def get_context_data(self, *args, **kwargs) :
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        qs = RestaurantLocation.objects.filter(owner=self.get_object())
        
        if qs.exists():
            context['locations'] = qs
        return context