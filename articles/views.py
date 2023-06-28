from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles_list.html', {'articles': articles})


def article_details(request , slug):
    return HttpResponse(slug)

