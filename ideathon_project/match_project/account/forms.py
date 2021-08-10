#UserCreationForm으로는 login.html에서 보여지는 테이블들을 보여주는데 한계가 있기 떄문에 해당 앱의 formsp.py를 통해 극복

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser 
        fields = ['username', 'password1', 'password2', 'nickname', 'location', 'university',]