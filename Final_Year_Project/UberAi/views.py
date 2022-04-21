from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request , 'home.html' , {'title' : 'Home'})

def app(request):
    return render(request , 'app.html' ,{'title' : 'App'})