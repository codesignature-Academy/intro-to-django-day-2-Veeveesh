from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# home — returns a response for the homepage.
# about — returns a response describing the app.
# contact — returns a response with some way to get in touch (a placeholder is fine)
def home(requests):
    return HttpResponse("<h1>This is our Texter Homepage <h1>")

def about(requests):
    return HttpResponse(f"<h1> You are currently in our about page<h1/> \n Texter is our first website used to find errors in your code")

def contact(requests):
    return HttpResponse(f" Get in touch with us via github - Veeveesh")