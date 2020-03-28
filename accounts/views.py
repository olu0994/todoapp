from django.shortcuts import render, redirect
from accounts.forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')


    if request.method == "POST":
        user = auth.authenticate(
           username=request.POST['username'].lower(),
           password=request.POST['password']
        )   
        if user is not None:
            # A BACKEND authenticated the credentials    
            auth.login(request,user)
            return redirect("home")
        else:
            # No backend authenticated the credentials    
            messages.error(request, "usernamr or password do not match our records.")
            return redirect("login")     


def signup(request):

    # when we make a GET request
    # usually from links
    if request.method == "GET":
        users = User.objects.all()
        context = {
            'user' : users,
        }
        return render(request, 'accounts/signup.html', context)

    # post request is executed when you want to store user data(usually from a form fields) 
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # process form value
            # if valid data create users objects
            user = User.objects.create_user(
                username=request.POST ['username'].lower(),
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                password=request.POST['password1'],
            ) 
            # if succesful get the succesful message and redirect to login page
            messages.success(request, 'Account creation was succesful')
            return redirect('login')  
        else:
            # return error message
            # if error return the error through a form ibject created above
            users = User.objects.all()
            context = {
                'form' : form,
                'user' : users,
            } 
            return render(request, 'accounts/signup.html', context)


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect("home")
    else:
        return redirect("home")          
