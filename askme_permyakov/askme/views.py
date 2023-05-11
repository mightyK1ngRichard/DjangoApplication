from django.contrib import auth
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound, Http404
from django.urls import reverse
from askme_permyakov.forms import LoginForm, RegistrationForm
from .models import *


def index(request):
    if request.method == 'POST':
        data = request.POST.get('searching_text')

        # Если data is None, значит форма пришла из создания поста.
        if data is None:
            user_title = request.POST.get('title')
            user_text = request.POST.get('text')
            user_tags = request.POST.get('tags[]')
            user_id = request.user.id

            # Если поля пустые, запись создана не будет. Делать проверки и писать про ошибки пока лень.
            if user_title == '' and user_text == '':
                posts = Posts.objects.all()
                return render(request, 'index.html', {'posts': posts})

            new_post = Posts.objects.create(title=user_title, content=user_text, author_id=user_id)
            for tag in user_tags:
                TagsOfPost.objects.create(post_id=new_post.id, tag_id=tag)

            return redirect(reverse('index'))

        # Если текст пользователя не пуст. Если пуст, вернём все посты.
        if data != '':
            posts = Posts.objects.filter(title__icontains=data)
            # Если найдены совпадения.
            if len(posts) != 0:
                return render(request, 'index.html', {'posts': posts})

    posts = Posts.objects.all()
    return render(request, 'index.html', {'posts': posts})


def create_post(request):
    tags = Tag.objects.all()
    return render(request, 'create_post.html', {'tags': tags})


def login_user(request):
    if request.method == 'GET':
        login_form = LoginForm()

    elif request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(request=request, **login_form.cleaned_data)
            if user:
                login(request, user)
                return redirect(reverse('index'))
            login_form.add_error(None, 'Invalid username or password')

    return render(request, 'login.html', {'form': login_form})


def post_with_tag(request, tag_id):
    posts_with_tag = [el.post for el in TagsOfPost.objects.filter(tag_id=tag_id)]
    return render(request, 'index.html', {'posts': posts_with_tag})


def register_user(request):
    if request.method == 'GET':
        user_form = RegistrationForm()
    elif request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            if user:
                # Создаём связь с таблицей авторы.
                user_profile = Author(user=user)
                user_profile.save()
                return redirect(reverse('index'))

            user_form.add_error(None, 'User saving error!')

    return render(request, 'register_user.html', {
        'form': user_form
    })


@login_required(login_url='/login/')
def user_page(request):
    return render(request, 'user_page.html')


def logout_user(request):
    logout(request)
    return redirect(reverse('index'))


def question(request, current_id):
    if request.method == 'POST':
        respond_content = request.POST.get('content')
        user_of_respond = request.user.id
        new_respond = Response.objects.create(content=respond_content, author_id=user_of_respond)
        ResponsesUnderPost.objects.create(post_id=current_id, response_id=new_respond.id)
        return redirect(reverse('question', args=[current_id]))

    post = get_object_or_404(Posts, pk=current_id)
    return render(request, 'detail_of_question.html', context={
        'post': post
    })
