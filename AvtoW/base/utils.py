from django.db.models import Count
from .models import *

menu = [{'title': "Мои заказы", 'upl_name': "orderlist"},
        {'title': "Отчет", 'upl_name': "otchet"},
        {'title': "О нас", 'upl_name': "about"},
        {'title': "Регистрация", 'upl_name': "login"}]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('product'))
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(0)
            user_menu.pop(0)
        elif not self.request.user.is_superuser:
            user_menu.pop(1)
        context['menu'] = user_menu
        context['cats'] = cats
        if 'selected' not in context:
            context['selected'] = 0
        return context
