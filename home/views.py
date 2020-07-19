from django.shortcuts import render, redirect
from .models import users
from django.contrib import messages

#TODO finish out success.html
#TODO log out link
#TODO 


def index(request):
    content = {
        'users': users.objects.all()
    }
    return render(request, 'index.html', content)

def fetch_users(request):
    content = {
        'users': users.objects.all()
    }
    return render(request, 'users.html', content)

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
        
        user = users.objects.get(email = email)
        request.session['userID'] = user.id #attaches userID into session to be used to access database
        return redirect('/success')
    else:
        #TODO error messegaes
        print("nah bitch")
        return redirect('/')

def success(request):
    if not 'userID' in request.session: #if no ones log in, redirect back to splash page
        return redirect('/')
    user = users.objects.get(id = request.session['userID'])
    contents = {
        'user': user
    }
    return render(request, 'success.html', contents)

def logout(request): #clears session
    request.session.clear()
    return render(request, 'loggedout.html')


