from django.contrib import admin
from django.urls import path
from .views import * # *는 해당 views의 모든것을 불러온다는 의미 -> 나중에 해당 내용을 from blog import views로 바꾸어도 되는지 해보자
# from blog import views # 성공!
# from blog.views import home, detail, new, create#성공! -> 해당 방법은 from blogs.views import *랑 비슷하지만 원하는 기능만 빼온다는 점에서 다름


urlpatterns = [
    path('<str:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('edit/<str:id>', edit, name="edit"),
    path('update/<str:id>', update, name="update"), #html에서 접급할 수 있는 name space
    path('delete/<str:id>', delete, name="delete"),
]