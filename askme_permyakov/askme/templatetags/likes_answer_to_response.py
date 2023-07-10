from django import template

from ..models import *

register = template.Library()

@register.simple_tag(takes_context=True)
def is_liked(context, blog_post_id):
    request = context['request']
    try:
        blog_likes = AnswerToResponseLikes.objects.get(blog_post_id=blog_post_id, liked_by=request.user.id).like
    except Exception as e:
        blog_likes = False
    return blog_likes

@register.simple_tag()
def count_likes(blog_post_id):
    return AnswerToResponseLikes.objects.filter(blog_post_id=blog_post_id, like=True).count()

@register.simple_tag(takes_context=True)
def blog_likes_id(context, blog_post_id):
    request = context['request']
    return AnswerToResponseLikes.objects.get(blog_post_id=blog_post_id, liked_by=request.user.id).id