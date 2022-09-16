from django.shortcuts import render
#from django.http import HttpResponse
import random

# Create your views here.
def about(request):
    return render(request, 'about.html')

def home(request): 
    return render(request, "home.html")  

def password(request):

    characters = list("abcdefghijklmnopqrstuvwxyz")
    generated_password = ""
    
    length = int(request.GET.get('length'))
    for char in range(length):
        generated_password += random.choice(characters)

    return render(request, "password.html", {"password": generated_password})    

