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
    return ResponsesUnderPost.objects.filter(post_id=post_id)


@register.simple_tag()
def get_author_info(user_id):
    author = Author.objects.get(user_id=user_id)
    count_post = Posts.objects.filter(author_id=author.id).count()
    count_responses = Response.objects.filter(author_id=author.id).count()
    return {'author': author, 'count_post': count_post, 'count_responses': count_responses}


@register.simple_tag()
def isAuthor(user_id, author_id):
    author = Author.objects.get(user_id=user_id)
    if author.pk == author_id:
        return True

    return False
