from django.db import models

INFO = [
    {
        'id': f'{i}',
        'logo': '',
        'title': f'Title {i}',
        'text': f'text {i}',
        'count_response': f'{i * 10}',
        'tags': [
            {
                'id_tag': f'{i2}',
                'name_tag': f'black_{i2}'
            } for i2 in range(i)
        ]
    } for i in range(10)
]


class Tags(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.ImageField(default='https://i.pinimg.com/originals/64/94/0c/64940cfc8514d44598287ab290905cf8.jpg')

    def __str__(self):
        return self.name


class Posts(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_public = models.DateField(auto_now=True)
    likes_count = models.IntegerField()
    tag_id = models.ForeignKey(Tags, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.title


class Response(models.Model):
    content = models.TextField()
    date_response = models.DateTimeField(auto_now=True)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class ResponsesUnderPost(models.Model):
    response_id = models.ForeignKey(Response, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
