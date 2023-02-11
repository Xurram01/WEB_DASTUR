from django.shortcuts import render

def news_home(requests):
    return render(requests, 'news/news_home.html')
