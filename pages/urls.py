from django.urls import path
# 현재 경로 (.) 에서 view를 가지고 와라! 
from . import views

urlpatterns = [
    # path('one/', views.one),
    # path('two/', views.two),

    path('static_example/', views.static_example),

    path('push_number/', views.push_number),
    path('pull_number/', views.pull_number),

    path('lotto_pick/', views.lotto_pick),
    path('lotto_result/', views.lotto_result),
    path('result/', views.result),
    path('search/', views.search),
    path('lotto/', views.lotto),
    path('isitbirthday/', views.isitbirthday),
    path('template_language/', views.template_language),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('greeting/<str:name>/', views.greeting),
    path('dinner/<str:name>/', views.dinner),
    path('introduce/', views.introduce),
    path('image/', views.image),
    path('index/', views.index),
]
