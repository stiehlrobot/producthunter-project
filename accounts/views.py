from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        #the user has info and wants account
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.get(username=request.POST['username'])
            return render(request, 'accounts/signup.html', {'error': 'Username has already been taken!'})
    else:
        #user wants to enter info
        return render(request, 'accounts/signup.html')

def login(request):

    return render(request, 'accounts/login.html')

def logout(request):
    #need to route to homepage
    #and dont forget to logout
    return render(request, 'accounts/signup.html')
