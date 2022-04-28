from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def profile(request):
    return HttpResponse("This is profile page.")