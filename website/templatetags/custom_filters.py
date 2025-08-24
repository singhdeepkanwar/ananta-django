# website/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter(name='splitlines')
def splitlines(value):
    """
    Splits a string by newlines.
    Useful for looping through lines from a TextField.
    """
    return value.splitlines()