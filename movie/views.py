from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title=searchTerm)
    else:
        movies = Movie.objects.all()
    return render( request , 'home.html',{
        'name':'Yash Vaibhav',
        'searchTerm':searchTerm,
        'movies':movies
    })

def about(request):
    return HttpResponse('<h1>Welcome to About page</h1>')

def signup(request):
    emailValue = request.GET.get('email')
    return render(request,'signup.html',{
        'email':emailValue
    })