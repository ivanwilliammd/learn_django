from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
def home(request):
    context = {
                "html_var" : "IvanMD",
                "num" : random.randint(1,100),
                "some_list" : [random.randint(1,10000), random.randint(1,1000), random.randint(1,100000)]
            }
    return render(request, 'base.html', context)
    # return HttpResponse('Hello, World!')