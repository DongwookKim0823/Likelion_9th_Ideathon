from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from common.forms import UserRegistrationForm
from common.models import User


def main(request):
    return render(request, 'main.html')

class UserRegistrationView(CreateView):
    model = get_user_model()
    form_class = UserRegistrationForm