from django import template
from base.models import *

register = template.Library()


@register.inclusion_tag('base/list_categories.html')
def show_categories(selected=0):
    cats = Category.objects.all()
    return {"cats": cats, "selected": selected}
