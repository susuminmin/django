from django.shortcuts import render
from datetime import datetime, date, time
import random


def index(request): # 첫번째 인자는 반드시 request 가 온다. => 사용자가 보내는 요청에 대한 정보
    # 요청이 들어오면 'index.html' 을 보여준다.
    return render(request, 'pages/index.html')    # render의 첫번째 인자도 반드시 request


def introduce(request):
    return render(request, 'pages/introduce.html')


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
    return render(request, 'pages/dinner.html', context)


def image(request):
    context = {
        'image_url': 'https://picsum.photos/500'  # str 은 ''로 감싸줘야 함
    }
    # image url 을 context 에 담아서 image.html 에 전달한다.
    return render(request, 'pages/image.html', context)


# 예를 들어... greeting/BTS/ 를 넣으면? name = 'BTS' 가 들어가 있음
def greeting(request, name):
    context = {
        'name': name
    }
    return render(request, 'pages/greeting.html', context)


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
    return render(request, 'pages/times.html', context)


def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber']
    datetimenow = datetime.now()
    empty_list = []  # empty 이기 때문에 가입한 유저가 없습니다 라고 표현됨

    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow
    }
    return render(request, 'pages/template_language.html', context)


def isitbirthday(request):
    return render(request, 'pages/isitbirthday.html')


def lotto(request):
    real_lottos = [21, 25, 30, 32, 40, 42]
    lottos = sorted(list(random.sample(range(1, 46), 6)))

    context = {
        'real_lottos': real_lottos,
        'lottos': lottos,
    }

    return render(request, 'pages/lotto.html', context)


def search(request):
    return render(request, 'pages/search.html')


def result(request):
    # print(request.GET)
    # <QueryDict: {'query': ['안녕하세요']}> => 꺼내서 쓸 수 있다는 의미
    category = request.GET.get('category')
    query = request.GET.get('query')
    context = {
        'query': query,
        'category': category,
    }
    return render(request, 'pages/result.html', context)


def lotto_pick(request):
    return render(request, 'pages/lotto_pick.html')


def lotto_result(request):
    numberList = request.GET.get('numberList')
    numberList = sorted(list(map(int, numberList.split())))
    # numberList = [int(number) for number in numberList.split()]
    realLottoNumbers = sorted([21, 25, 30, 32, 40, 42])
    # if realLottoNumbers == numberList:
    #     result = '퇴사합시다! 고생하셨습니다!'
    # else:
    #     result = '야근합시다!!'
    context = {
        'numberList': numberList,
        'realLottoNumbers': realLottoNumbers,
        # 'result': result,
    }
    return render(request, 'pages/lotto_result.html', context)


def static_example(request):
    return render(request, 'pages/static_example.html')


def push_number(request):
    return render(request, 'pages/push_number.html')


def pull_number(request):
    pull_number = request.GET.get('pull_number')
    # pull_number = str(pull_number)
    context = {
        'pull_number': pull_number,
    }
    return render(request, 'pages/pull_number.html', context)


def one(request):
    return render(request, 'pages/one.html')


def two(request):
    return render(request, 'pages/two.html')

# def hello(request, name):
# 	context = {
#         'name': name,	
# 	}
#     return render(request, 'hello.html', context)
