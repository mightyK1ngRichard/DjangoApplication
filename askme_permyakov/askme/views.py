from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound, Http404
from .models import *


def index(request):
    posts = Posts.objects.all()
    return render(request, 'index.html', {
        'posts': posts
    })


def question(request, current_id):
    post = get_object_or_404(Posts, pk=current_id)

    return render(request, 'detail_of_question.html', context={
        'post': post
    })


def tempAPI(request):
    return HttpResponse('Проверка')
