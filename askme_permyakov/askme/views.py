from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound, Http404
from .models import Author, Tags, Response, ResponsesUnderPost, Posts


def index(request):
    info = Posts.objects.all()
    context = {
        'info': info
    }
    return render(request, 'index.html', context=context)


def question(request, current_id):
    info = Posts.objects.all()
    current_question = list(filter(lambda x: x['id'] == current_id, info))
    if len(current_question) == 0:
        return Http404

    return render(request, 'index.html', context={
        'info': info,
        'count_question': len(info)  # TODO: сделать логику.
    })


def tempAPI(request):
    return HttpResponse('Проверка')
