from django import template
from django.utils.html import format_html
import re

register = template.Library()


@register.filter
def clean_messages(value):
    message_lis = ''
    messages = re.findall(r'.<ul class="errorlist"><li>(.*?)</li></ul>', str(value))
    if messages:
        for message in messages:
            message_lis += message + '</br>'
        return format_html(message_lis)
    else:
        return format_html(str(value))
