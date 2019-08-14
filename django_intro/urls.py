"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
# 경로 보고 불러온다. pages 앱에서 views.py 데려옴
from pages import views

# 맞는 예시: www.ssafy.com/admin/ => 성공
# 틀린 예시: www.ssafy.com/login/ => 페이지 없음

urlpatterns = [
    # path('login/', 로그인 페이지 관련 함수) 가 있어야 이쪽으로 이동시킬 수 있음 / 사용자에게 어떤 페이지 보여줄지 이 안에서 결정됨

    # 경로 적는 순서도 중요 / 위 ~ 아래에서 작성되도록 한다. (중복될 경우 위에 있는 것만...)

    # path('사용자가 접속하는 경로)
    # <> 하면 변수로서 활용
    path('times/<int:num1>/<int:num2>/', views.times),
    path('greeting/<str:name>/', views.greeting),
    path('dinner/<str:name>/', views.dinner),
    path('index/', views.index),
    path('introduce/', views.introduce),
    path('image/', views.image),
    path('admin/', admin.site.urls),
]
# 우리가 접속할 수 있는 url을 정의하는 곳이라고 생각하면된다.
