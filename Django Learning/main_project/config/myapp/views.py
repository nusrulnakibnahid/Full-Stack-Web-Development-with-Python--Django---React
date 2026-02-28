from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Django, I am Nahid")


def profile(request):
    return HttpResponse("This is my profile page")


def dashboard(request):
    return HttpResponse("This is my dashboard page")



def about(request):
    return render(request, 'about.html')