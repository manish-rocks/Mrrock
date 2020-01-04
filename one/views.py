from django.shortcuts import render

# Create your views here.
from .models import (Cake_Category)

def contact(request):
    return render(request,"user-page/contact.html",{})

def food(request):
    return render(request,"user-page/LHD FOOD.html",{})

def basket(request):
    return render(request,"user-page/LHD BASKET.html",{})
def myadmin(request):
    return render(request,"user-page/dashboard.html",{})


def dashboard(request):
    return render(request,"Dashboard.html",{})
def application_setup(request):
    return render(request,"Application-setup",{})
def new_order(request):
    return render(request,"New-Order.html",{})
def check_online_order(request):
    return render(request,"Check-Online-Order.html",{})
def tracking(request):
    return render(request,"Tracking.html",{})
def reports(request):
    return render(request,"Reports.html",{})
def counter(request):
    return render(request,"Counter.html",{})
def logout(request):
    return render(request,"Logout.html",{})
