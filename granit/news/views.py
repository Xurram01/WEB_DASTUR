from django.shortcuts import render
from .models import Articles

def news_home(requests):
    news = Articles.objects.order_by('-date')
    return render(requests, 'news/news_home.html', {'news': news})
 def create(request):
     return render(request, 'news/create.html')