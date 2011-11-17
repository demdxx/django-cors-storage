from django import  template

from ..tracker import tracker

register = template.Library()

@register.filter
def corstorage_record(name,values=None):
    if values:
        name = name % values

    result = None
    for key in name.split('.'):
        result = tracker[key] if not result else result[key]
        if not result:
            break
    return result
