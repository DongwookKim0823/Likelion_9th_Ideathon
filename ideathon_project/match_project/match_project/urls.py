"""lionproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from match.views import * # 는 해당 views의 모든것을 불러온다는 의미 -> 나중에 해당 내용을 from blog import views로 바꾸어도 되는지 해보자
# from blog import views # 성공!
# from blog.views import home, detail, new, create#성공! -> 해당 방법은 from blogs.views import 랑 비슷하지만 원하는 기능만 빼온다는 점에서 다름
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('match/', include('match.urls')),
    path('account/', include('account.urls')), #blog/templates에 있는 urls.py의 경로가 blog/[] <- 해당위치에 오게됨.
    #include()를 통해 url을 효과적으로 관리할 수 있음. 위에 path 옆에 include를 같이 import해주어야함.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #해당 코드의 settings는 setting.py와 다르다.
