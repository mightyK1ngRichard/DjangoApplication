from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='static/img', default='static/img/default.webp')

    def __str__(self):
        return self.user.username


class Posts(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_public = models.DateField(auto_now=True)
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
