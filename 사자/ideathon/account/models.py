from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser): # 해당 프로젝트 setting.spy urls.py 주석처리 해주고 makemigratinos, migrate해주어야함
    nickname = models.CharField(max_length=10)
    
