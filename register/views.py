from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.


def home(Response):
    return render(Response, "register/index.html")


def signin(Response):

    if Response.method == "POST":
        username = Response.POST.get("username")
        password = Response.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(Response, user)
            return render(Response, "register/signout.html", {"username": username})

        else:
            messages.error(Response, "False infos")
            return redirect("home")

    return render(Response, "register/signin.html")


def signup(Response):

    if Response.method == "POST":
        username = Response.POST.get("username")
        email = Response.POST.get("email")
        password = Response.POST.get("password")

        myuser = User.objects.create_user(username, email, password)
        myuser.save()

        messages.success(Response, "Your account create successfully")
        return redirect("signin")

    return render(Response, "register/signup.html")


def signout(Response):
    return render(Response, "register/signout.html")
