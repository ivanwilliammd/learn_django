from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")

def profile(request):
    return HttpResponse("This is profile page.")