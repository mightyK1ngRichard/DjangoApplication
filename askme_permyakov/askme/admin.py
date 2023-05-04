from django.contrib import admin
from . import models

admin.site.register(models.Tags)
admin.site.register(models.Author)
admin.site.register(models.Posts)
admin.site.register(models.Response)
admin.site.register(models.ResponsesUnderPost)
