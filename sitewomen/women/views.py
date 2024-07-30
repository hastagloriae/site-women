from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Сторінка додатку Women")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Категорії</h1><p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Категорії</h1><p>slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2024:
        return redirect('home')

    return HttpResponse(f"<h1>Архів</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Сторінки не існує</h1>")