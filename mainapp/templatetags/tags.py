from django import template

register = template.Library()


@register.filter(name='size_checker')
def size_checker(text):
    size = len(text)
    if size > 300:

        return text[:300]
    elif size < 300:
        text += (' &nbsp;' * (300 - size))
        return text
    return text
