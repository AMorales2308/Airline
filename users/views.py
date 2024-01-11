from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse 
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    # Si no hay un usuario iniciado, retirna a la página de login
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request, "users/user.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Revisa si el usuario y la contraseña son correctos, retorna un objeto usuario si es así
        user = authenticate(request, username=username, password=password)

        # Si se retorna un objeto usuario, se loguea y dirige a la página del index
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("users:index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid Credentials"
            })

    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged Out"
    })