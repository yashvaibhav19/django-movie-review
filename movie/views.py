from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    searchTerm = request.GET.get('searchMovie')
    return render( request , 'home.html',{
        'name':'Yash Vaibhav',
        'searchTerm':searchTerm
    })

def about(request):
    return HttpResponse('<h1>Welcome to About page</h1>')

def signup(request):
    emailValue = request.GET.get('email')
    return render(request,'signup.html',{
        'email':emailValue
    })