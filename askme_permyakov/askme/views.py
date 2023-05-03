from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound, Http404
from . import models


def index(request):
    context = {
        'info': models.INFO
    }
    return render(request, 'index.html', context=context)


def question(request, current_id):
    current_question = list(filter(lambda x: x['id'] == current_id, models.INFO))
    if len(current_question) == 0:
        return Http404

    context = {
        'info': current_question
    }
    return render(request, 'index.html', context=context)


def tempAPI(request):
    return HttpResponse('Проверка')
