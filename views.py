from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from django.views import View


def home(request):
    params = {
        'phrase': '_________ИностраН!_______________'
    }
    return render(request, 'home.html', context=params)

feed_data = [
        {
            'id': '1',
            'image': 'https://pp.vk.me/c418629/v418629769/727/OtGPEPmjdLQ.jpg',
            'likes_count': 36,
            'username': 'RomeoSANREMO',
            'text': 'ЭлитаС',
            'published': date(2016, 11, 1)
        },
        {
            'id': '2',
            'image': 'https://im2-tub-ru.yandex.net/i?id=7834e2e973c7281fd2060fea941471be&n=33&h=215&w=323',
            'likes_count': 10,
            'username': 'MichaForever',
            'text': 'BMWешечка',
            'published': date(2016, 11, 6)
        },
        {
            'id': '3',
            'image': 'http://www.coollady.ru/puc/3/zima/b/004.jpg',
            'likes_count': 23,
            'username': 'GorillaЗубрила',
            'text': 'Kлассная природа',
            'published': date(2016, 1, 3)
        },
        {
            'id': '4',
            'image': 'https://d1w5usc88actyi.cloudfront.net/wp-content/uploads/2013/09/Fstoppers-Kiliii-Fish-climbing-photo3.jpg',
            'likes_count': 344,
            'username': 'Sohi',
            'text': 'Экстриммммм',
            'published': date(2016, 1, 3)
        },
        {
            'id': '5',
            'image': 'http://img.youtube.com/vi/zJGnKgICMqU/0.jpg',
            'likes_count': 267,
            'username': 'Goley',
            'text': 'Дневник',
            'published': date(2016, 1, 3)
        },
        {
            'id': '6',
            'image': 'http://www.kralsinema.com/uploads/oyuncu/2016/05/tim-burton-605.jpg',
            'likes_count': 91,
            'username': 'Jalа',
            'text': 'Тим!',
            'published': date(2016, 1, 3)
        },
    ]

def feed(request):
    # Получение ленты пользователя
    # ...


    return render(request, 'feed1.html', context={'feed': feed_data})

class User(View):
     def get(self, request, id):
         user = None
         for item in feed_data:
             if item['id'] == id:
                 user = item
         if not user:
             raise Http404
         return render(request, 'Users.html', context=user)