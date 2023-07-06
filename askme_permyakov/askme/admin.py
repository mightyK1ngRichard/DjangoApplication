from django.contrib import admin
from . import models

admin.site.register(models.Tag)
admin.site.register(models.TagsOfPost)
admin.site.register(models.Author)
admin.site.register(models.Posts)
admin.site.register(models.Response)
admin.site.register(models.ResponsesUnderPost)
admin.site.register(models.BlogLikes)
admin.site.register(models.AnswerLikes)