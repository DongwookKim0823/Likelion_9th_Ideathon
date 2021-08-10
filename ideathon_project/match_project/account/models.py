from django.db import models
from django.contrib.auth.models import AbstractUser #유저 테이블을 장고에서 제공되는 것이 아닌 원하는 유저 테이블로 상속시켜서 바꿔치기 하기 위함
# Create your models here.                          #setting.py에 AUTH_USERMODEL도 추가해줘야한다.

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    location = models.CharField(max_length=200)

