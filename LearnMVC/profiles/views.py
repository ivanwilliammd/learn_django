from re import U
from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

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