__author__ = 'gnuhpc'
from django import template
import datetime

register = template.Library()

@register.filter
def add_prefix(value, arg):
    return "%s_%s" % (arg, value)

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)
