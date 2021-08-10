from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
            
        return redirect('home')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method =="POST":
        # form = UserCreationForm(request.POST) #django에서 정의되어있던 UserCreationForm 대신 RegisterForm이란 임의의 클래스로 대체한다. 로그인창에 항목들이 늘어남.
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
        return redirect('home')
    else:

        # form = UserCreationForm()
        form = RegisterForm()
        return render(request, 'signup.html', {'form':form})