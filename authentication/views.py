from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home (request):
    return render (request, "authentication/index.html")

def signup (request):

    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_lane =  lname

        myuser.save()

        messages.success(request, "Your account has been successfully created.")

        return redirect('signin')

    return render (request, "authentication/signup.html")

def signin (request):
    return render (request, "authentication/signin.html")

def signout (request):
    pass