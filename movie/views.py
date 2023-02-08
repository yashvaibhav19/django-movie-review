from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Welcome to Home page')

def about(request):
    return HttpResponse('<h1>Welcome to About page</h1>')