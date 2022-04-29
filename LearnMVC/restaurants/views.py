from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
def home(request):
    context = {
                "title" : "IvanMD",
                "section" : "Home",
                "num" : random.randint(1,100),
                "some_list" : [random.randint(1,10000), random.randint(1,1000), random.randint(1,100000)]
            }
    return render(request, 'home.html', context)
    # return HttpResponse('Hello, World!')

def about(request):
    context = {
                "title" : "IvanMD",
                "section" : "About",
            }
    return render(request, 'about.html', context)

def contact(request):
    context = {
                "title" : "IvanMD",
                "section" : "Contact",
            }
    return render(request, 'contact.html', context)