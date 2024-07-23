from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Сторінка додатку Women")


def categories(request):
    return HttpResponse("<h1>Категорії</h1>")
