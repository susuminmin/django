# pages/views.py
from django.shortcuts import render
import random

# Create your views here. 중요!
# 뷰함수 => 사용자에게 보여주는 페이지 명세


def index(request):             # 첫번째 인자는 반드시 request 가 온다. => 사용자가 보내는 요청에 대한 정보
    # 요청이 들어오면 'index.html' 을 보여준다.
    return render(request, 'index.html')    # render의 첫번째 인자도 반드시 request


def introduce(request):
    return render(request, 'introduce.html')


# Template Variable Example
def dinner(request, name):
    menu = ['강남 더막창스', '노랑통닭', '양자강']
    pick = random.choice(menu)
    context = {
        'name': name,
        'pick': pick,
    }

    # Django template 으로 context 전달
    # dinner.html 로 context 를 넘김
    return render(request, 'dinner.html', context)


def image(request):
    context = {
        'show': 'https://picsum.photos/500'  # str 은 ''로 감싸줘야 함
    }
    # image url 을 context 에 담아서 image.html 에 전달한다.
    return render(request, 'image.html', context)


# 예를 들어... greeting/BTS/ 를 넣으면? name = 'BTS' 가 들어가 있음
def greeting(request, name):
    context = {
        'name': name
    }
    return render(request, 'greeting.html', context)


def times(request, num1, num2):
    if num1 == 1 and num2 == 1:
        context = {
            'num1': num1,
            'num2': num2,
            'result': '창문',
        }
    else:
        context = {
            'num1': num1,
            'num2': num2,
            'result': num1 + num2
        }
    return render(request, 'times.html', context)
