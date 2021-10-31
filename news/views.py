from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import News

# Create your views here.
def index(request) :
    news = News.objects.all()
    context = {
        'news' : news
    }
    return render(request,'news/news.html',context)


def article(request,news_id):
    recent = News.objects.all()[:5]
    article = get_object_or_404(News,pk=news_id)
    context = {
        'article' : article,
        'recent' : recent
    }
    return render(request,'news/article.html',context)