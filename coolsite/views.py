from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'women/index.html', {'menu': menu, 'title': 'О сайте'})

def categories(request, carotid):
    if (request.GET):
        print(request.GET)

    return HttpResponse(f"<h1>Статьи по категориям</h1>{carotid}</p>")

def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")

