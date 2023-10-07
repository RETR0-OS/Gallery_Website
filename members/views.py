from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return redirect("https://online.vidyamandir.com/user/login")
    else:
        return render(request, "authentication/login.html")

@login_required
def logout_user(request):
    logout(request)
    return redirect("home")
