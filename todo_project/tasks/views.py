from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>This is our Texter Homepage <h1>")

def about(request):
    return HttpResponse(f"<h1> You are currently in our about page<h1/> \n Texter is our first website used to find errors in your code")

def contact(request):
    return HttpResponse(f" Get in touch with us via github - Veeveesh")