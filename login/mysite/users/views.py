from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import User
# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증성공")
            login(request, user)
            return render(request, "main.html")
        else:
            print("인증실패")


    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "main.html")

def signup_view(request):

    if request. method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        user_id = request.POST["user_id"]

        user = User.objects.create_user(username, email, password)
        user.last_name = lastname
        user.first_name = firstname
        user.user_id = user_id
        user.save()

        return render(request, "main.html")

    return render(request, "users/signup.html")