from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from common.views import UserRegistrationView

app_name = 'common'

urlpatterns = [
    path('', views.main, name='main' ),
    path('create/', UserRegistrationView.as_view()),
]