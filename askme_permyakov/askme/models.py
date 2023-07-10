from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.TextField(default='https://firebasestorage.googleapis.com/v0/b/digitalstackoverflow.appspot.com/o/avatars%2Fdefault.jpg?alt=media', max_length=500)

    def __str__(self):
        return self.user.username


class Posts(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_public = models.DateTimeField(auto_now=True)
    likes_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class TagsOfPost(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class Response(models.Model):
    content = models.TextField()
    date_response = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class ResponsesUnderPost(models.Model):
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)


class BlogLikes(models.Model):
    blog_post = models.ForeignKey(Posts, on_delete=models.CASCADE, null=True)
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    like = models.BooleanField('Like', default=False)
    created = models.DateTimeField('Дата и время', default=timezone.now)

    def __str__(self):
        return f'{self.liked_by}: {self.blog_post} {self.like}'

    class Meta:
        verbose_name = 'Blog Like'
        verbose_name_plural = 'Blog Likes'


class AnswerLikes(models.Model):
    blog_post = models.ForeignKey(Response, on_delete=models.CASCADE, null=True)
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    like = models.BooleanField('Like', default=False)
    created = models.DateTimeField('Дата и время', default=timezone.now)

    def __str__(self):
        return f'{self.liked_by}: {self.blog_post} {self.like}'

    class Meta:
        verbose_name = 'Answer Like'
        verbose_name_plural = 'Answer Likes'


class AnswerToResponse(models.Model):
    content = models.TextField()
    date_response = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    whom_to_answer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    response_parent = models.ForeignKey(Response, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.content} + {self.id}'


class AnswerToResponseLikes(models.Model):
    blog_post = models.ForeignKey(AnswerToResponse, on_delete=models.CASCADE, null=True)
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    like = models.BooleanField('Like', default=False)
    created = models.DateTimeField('Дата и время', default=timezone.now)

    def __str__(self):
        return f'{self.liked_by}: {self.blog_post} {self.like}'

    class Meta:
        verbose_name = 'AnswerToResponse Like'
        verbose_name_plural = 'AnswerToResponse Likes'