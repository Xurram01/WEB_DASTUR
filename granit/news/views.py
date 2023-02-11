from django.shortcuts import render

def news_home(requests):
    return render(requests, 'main/about.html')
