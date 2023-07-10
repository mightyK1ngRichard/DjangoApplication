import os
import re
from django.contrib import auth
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound, Http404
from django.urls import reverse
from askme_permyakov import settings
from askme_permyakov.forms import LoginForm, RegistrationForm, ChangePasswordForm
from .models import *
from django.shortcuts import redirect
from django.views.generic import View

import pyrebase

# Не взламывайте нас пж
firebaseConfig = {
    "apiKey": "AIzaSyAmL1FH_pTVm3Ie_TJ9KoDcqV8GHMzTU4o",
    "authDomain": "digitalstackoverflow.firebaseapp.com",
    "projectId": "digitalstackoverflow",
    "storageBucket": "digitalstackoverflow.appspot.com",
    "messagingSenderId": "574176527139",
    "appId": "1:574176527139:web:78f055071d49f11b230296",
    "measurementId": "G-R47DYRG10P",
    "databaseURL": "https://console.firebase.google.com/u/0/project/digitalstackoverflow/database/digitalstackoverflow-default-rtdb/data/~2F",
}

firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()


def index(request):
    if request.method == 'POST':
        data = request.POST.get('searching_text')
        # Если data is None, значит форма пришла из создания поста.
        if data is None:
            user_title = request.POST.get('title')
            user_text = request.POST.get('text')
            user_tags = request.POST.getlist('tags[]')
            user_custom_tags = request.POST.get('custom_tags', '')
            user_custom_tags = user_custom_tags.split(',')
            for tag_name in user_custom_tags:
                tag_name = tag_name.strip()  # Удаление лишних пробелов
                if tag_name:
                    tag, _ = Tag.objects.get_or_create(name=tag_name)
                    user_tags.append(tag.id)
            author = Author.objects.get(user_id=request.user.id)
            # Если поля пустые, запись создана не будет. Делать проверки и писать про ошибки пока лень.
            if user_title == '' and user_text == '':
                posts = Posts.objects.all()
                return render(request, 'index.html', {'posts': posts})

            new_post = Posts.objects.create(title=user_title, content=user_text, author_id=author.id)

            for tag_id in user_tags:
                tag = Tag.objects.get(id=tag_id)
                TagsOfPost.objects.create(post=new_post, tag=tag)

            return redirect(reverse('index'))

        # Если текст пользователя не пуст. Если пуст, вернём все посты.
        if data != '':
            posts = Posts.objects.filter(title__icontains=data)
            # Если найдены совпадения.
            if len(posts) != 0:
                return render(request, 'index.html', {'posts': posts})

    page_number = request.GET.get('page')

    # Самодельный пагинатор.
    # if page_number is None:
    #     page_number = 1
    # offset = (int(page_number) - 1) * 10
    # posts = Posts.objects.all().order_by('-date_public')[offset:offset+10]

    posts = Posts.objects.all().order_by('-date_public')
    paginator = Paginator(posts, 5)
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'posts': page_obj})


def update_post(request, current_id):
    if request.method == 'POST':
        post = Posts.objects.get(id=current_id)
        user_title = request.POST.get('title')
        user_text = request.POST.get('text')
        user_tags = request.POST.getlist('tags[]')
        user_custom_tags = request.POST.get('custom_tags', '')
        user_custom_tags = user_custom_tags.split(',')
        for tag_name in user_custom_tags:
            tag_name = tag_name.strip()  # Удаление лишних пробелов
            if tag_name:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                user_tags.append(tag.id)
        if user_title == '' and user_text == '':
            return redirect('question', current_id=post.id)

        post.title = user_title
        post.content = user_text
        post.save()
        existing_tags = TagsOfPost.objects.filter(post=post)
        existing_tag_ids = list(existing_tags.values_list('tag_id', flat=True))
        tags_to_add = [tag_id for tag_id in user_tags if tag_id not in existing_tag_ids]
        tags_to_remove = [tag_id for tag_id in existing_tag_ids if tag_id not in user_tags]
        TagsOfPost.objects.filter(post=post, tag_id__in=tags_to_remove).delete()

        for tag_id in tags_to_add:
            tag = Tag.objects.get(id=tag_id)
            TagsOfPost.objects.create(post=post, tag=tag)

        return redirect('question', current_id=post.id)
    else:
        post = get_object_or_404(Posts, id=current_id)
        tags = Tag.objects.all()
        selected_tags = TagsOfPost.objects.filter(post=post)
        selected_tags_name = [tag.tag.name for tag in selected_tags]
        return render(request, 'update_post.html', {'post': post, 'tags': tags, 'selected_tags': selected_tags_name})


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


@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return render(request, 'user/user_page.html')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'change_password.html', {'form': form})


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

            user_form.add_error(None, 'user saving error!')

    return render(request, 'user/register_user.html', {
        'form': user_form
    })


@login_required(login_url='/login/')
def user_page(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        user = User.objects.get(id=user_id)
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        avatar = request.FILES.get('avatar')
        if avatar:
            filename2 = avatar.name
            extension = re.findall(r'\.([^.]+)$', filename2)
            filename: str
            if extension:
                author = Author.objects.get(user_id=user_id)
                filename = f'avatar_{user.id}.{extension[0]}'
                # filepath = os.path.join(settings.STATIC_URL, 'img', filename)
                # author.avatar = filepath
                # # Сохраняем файл
                # with open(filepath, 'wb') as f:
                #     for chunk in avatar.chunks():
                #         f.write(chunk)


                # Сохраняем файл в Firebase Storage
                storage.child("avatars").child(filename).put(avatar)
                url = storage.child("avatars").child(filename).get_url(None)
                author.avatar = url

                author.save()

        return redirect(reverse('user_page'))

    return render(request, 'user/user_page.html')


def delete_account(request):
    user = request.user
    user.delete()

    logout(request)
    return redirect('index')


def user_page_by_id(request, user_id):
    author = Author.objects.get(user_id=user_id)
    posts = Posts.objects.all().filter(author_id=author.id)
    return render(request, 'user/user_page_by_id.html', {'user_id': user_id, 'posts': posts})


def logout_user(request):
    logout(request)
    return redirect(reverse('index'))


def question(request, current_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content != '':
            if request.POST.get('response_or_answer') == 'response':
                author = Author.objects.get(user_id=request.user.id)
                new_respond = Response.objects.create(content=content, author_id=author.id)
                ResponsesUnderPost.objects.create(post_id=current_id, response_id=new_respond.id)
            elif request.POST.get('response_or_answer') == 'answer':
                author = Author.objects.get(user_id=request.user.id)
                whom_to_answer = request.POST.get('whom_to_answer')
                author_to_answer = Author.objects.get(user_id=whom_to_answer)
                resp_id = request.POST.get('resp_id')
                AnswerToResponse.objects.create(content=content, author_id=author.id,
                                                whom_to_answer_id=author_to_answer.user.id, response_parent_id=resp_id)
        return redirect(reverse('question', args=[current_id]))

    post = get_object_or_404(Posts, pk=current_id)
    return render(request, 'detail_of_question.html', context={
        'post': post
    })


def delete_post(request):
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        responses = ResponsesUnderPost.objects.filter(post_id=post_id)

        # Удаляем все комментарии поста.
        for el in responses:
            Response.objects.get(pk=el.response_id).delete()
        Posts.objects.get(pk=post_id).delete()
        return redirect(reverse('index'))


def delete_respond(request):
    if request.method == 'POST':
        respond_id = request.POST.get('respond_id')
        post_id = request.POST.get('post_id')
        Response.objects.get(pk=respond_id).delete()

        return redirect(reverse('question', args=[post_id]))


def delete_answer(request):
    if request.method == 'POST':
        answer_id = request.POST.get('answer_id')
        response_id = request.POST.get('response_id')
        RespUndPost = ResponsesUnderPost.objects.get(response_id=response_id)
        post_id = RespUndPost.post_id
        AnswerToResponse.objects.get(pk=answer_id).delete()

        return redirect(reverse('question', args=[post_id]))


def users(request):
    all_users = Author.objects.all()
    return render(request, 'user/user.html', {'users': all_users})


def main(request):
    return render(request, 'main.html')


class AddLikeView(View):
    def post(self, request, *ags, **kwargs):
        blog_post_id = request.POST.get('blog_post_id')
        user_id = request.POST.get('user_id')
        url_from = request.POST.get('url_from')

        user_inst = User.objects.get(id=user_id)
        blog_post_inst = Posts.objects.get(id=blog_post_id)

        try:
            blog_like_inst = Posts.objects.get(blog_post=blog_post_inst, liked_by=user_inst)
        except Exception as e:
            blog_like = BlogLikes(blog_post=blog_post_inst, liked_by=user_inst, like=True)
            blog_like.save()
        return redirect(url_from)


class RemoveLikeView(View):
    def post(self, request, *args, **kwargs):
        blog_likes_id = request.POST.get('blog_likes_id')
        url_from = request.POST.get('url_from')
        blog_like = BlogLikes.objects.get(id=blog_likes_id)
        blog_like.delete()

        return redirect(url_from)


class AddLikeAnswerView(View):
    def post(self, request, *ags, **kwargs):
        blog_post_id = request.POST.get('blog_post_id')
        user_id = request.POST.get('user_id')
        url_from = request.POST.get('url_from')

        user_inst = User.objects.get(id=user_id)
        blog_post_inst = Response.objects.get(id=blog_post_id)

        try:
            blog_like_inst = Response.objects.get(blog_post=blog_post_inst, liked_by=user_inst)
        except Exception as e:
            blog_like = AnswerLikes(blog_post=blog_post_inst, liked_by=user_inst, like=True)
            blog_like.save()
        return redirect(url_from)


class RemoveLikeAnswerView(View):
    def post(self, request, *args, **kwargs):
        blog_likes_id = request.POST.get('blog_likes_id')
        url_from = request.POST.get('url_from')
        blog_like = AnswerLikes.objects.get(id=blog_likes_id)
        blog_like.delete()

        return redirect(url_from)


class AddLikeAnswerToResponseView(View):
    def post(self, request, *ags, **kwargs):
        blog_post_id = request.POST.get('blog_post_id')
        user_id = request.POST.get('user_id')
        url_from = request.POST.get('url_from')

        user_inst = User.objects.get(id=user_id)
        blog_post_inst = AnswerToResponse.objects.get(id=blog_post_id)

        try:
            blog_like_inst = AnswerToResponse.objects.get(blog_post=blog_post_inst, liked_by=user_inst)
        except Exception as e:
            blog_like = AnswerToResponseLikes(blog_post=blog_post_inst, liked_by=user_inst, like=True)
            blog_like.save()
        return redirect(url_from)


class RemoveLikeAnswerToResponseView(View):
    def post(self, request, *args, **kwargs):
        blog_likes_id = request.POST.get('blog_likes_id')
        url_from = request.POST.get('url_from')
        blog_like = AnswerToResponseLikes.objects.get(id=blog_likes_id)
        blog_like.delete()

        return redirect(url_from)
