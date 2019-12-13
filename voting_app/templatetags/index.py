# из http://stackoverflow.com/a/29664945/2714931
from django import template
register = template.Library()

@register.filter
def index(indexable, i):
    return indexable[i]