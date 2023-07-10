# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
from django import template
from askme.models import *
from django.template.defaultfilters import stringfilter
import markdown as md

register = template.Library()


@register.simple_tag()
def get_tags(post_id):
    return TagsOfPost.objects.filter(post_id=post_id)


@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.abbr',
        'markdown.extensions.attr_list',
        'markdown.extensions.def_list',
        'markdown.extensions.fenced_code',
        'markdown.extensions.footnotes',
        'markdown.extensions.md_in_html',
        'markdown.extensions.tables',
        'markdown.extensions.admonition',
        'markdown.extensions.codehilite',
        'markdown.extensions.legacy_attrs',
        'markdown.extensions.legacy_em',
        'markdown.extensions.meta',
        'markdown.extensions.nl2br',
        'markdown.extensions.sane_lists',
        'markdown.extensions.smarty',
        'markdown.extensions.toc',
        'markdown.extensions.wikilinks',
    ])


@register.simple_tag()
def get_responses_under_post(post_id):
    return ResponsesUnderPost.objects.filter(post_id=post_id).order_by('-response__date_response')


@register.simple_tag()
def get_author_info(user_id):
    author = Author.objects.get(user_id=user_id)
    count_post = Posts.objects.filter(author_id=author.id).count()
    count_responses = Response.objects.filter(author_id=author.id).count()
    count_responses += AnswerToResponse.objects.filter(author_id=author.id).count()
    author_posts = Posts.objects.filter(author_id=author.id)
    count_likes = 0
    for post in author_posts:
        count_likes += BlogLikes.objects.filter(blog_post_id=post.id).count()
    author_responses = Response.objects.filter(author_id=author.id)
    for response in author_responses:
        count_likes += AnswerLikes.objects.filter(blog_post_id=response.id).count()
    author_answers = AnswerToResponse.objects.filter(author_id=author.id)
    for answer in author_answers:
        count_likes += AnswerToResponseLikes.objects.filter(blog_post_id=answer.id).count()
    return {'author': author, 'count_post': count_post, 'count_responses': count_responses, 'count_likes': count_likes}


@register.simple_tag()
def isAuthor(user_id, author_id):
    author = Author.objects.get(user_id=user_id)
    if author.pk == author_id:
        return True

    return False


@register.simple_tag()
def get_answer_under_response(response_id):
    return AnswerToResponse.objects.filter(response_parent=response_id).order_by('date_response')



@register.simple_tag()
def get_count_answer_full(responses):
    count = responses.count()
    for response in responses:
        count += AnswerToResponse.objects.filter(response_parent=response.id+2).count()
    return count