from django.shortcuts import render, redirect
from .models import users
from django.contrib import messages

#set up index
#set up form
def index(request):
    return render(request, 'index.html')

def registerUser(request):
    
    #TODO redirect to first page after log in 

    errors = users.objects.validator(request.POST)
        
    if len(errors)> 0: #if error is not empty, submit errors and return to '' url
        for field, value in errors.items():
            messages.error(request, value, extra_tags='register')
        return redirect('/')
    else:
        users.objects.register(request.POST)
        return redirect('/')

def login(request):
    email = request.POST['email']
    pwd = request.POST['password']
    if users.objects.authenticator(email, pwd):
        #TODO load user id into session
        return render(request, 'success.html')
    else:
        #TODO error messegaes
        print("nah bitch")
        return redirect('/')