# path import
from django.urls import path
# 같은 app 내 view 함수
from . import views

# /utilities/ _____ : 다음에 올 것들이 온다. 
urlpatterns = [
    path('index/', views.index),
]
