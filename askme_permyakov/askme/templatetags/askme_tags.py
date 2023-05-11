# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
from django import template
from askme.models import *

register = template.Library()


@register.simple_tag()
def get_tags(post_id):
    return TagsOfPost.objects.filter(post_id=post_id)


@register.simple_tag()
def get_responses_under_post(post_id):
    return ResponsesUnderPost.objects.filter(post_id=post_id)


@register.simple_tag()
def get_author_info(user_id):
    author = Author.objects.get(user_id=user_id)
    count_post = Posts.objects.filter(author_id=author.id).count()
    count_responses = Response.objects.filter(author_id=author.id).count()
    return {'author': author, 'count_post': count_post, 'count_responses': count_responses}
