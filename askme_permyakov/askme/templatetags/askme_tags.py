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
