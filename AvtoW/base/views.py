from django.shortcuts import render

import base.views
from .models import *
from django.views.generic import *

menu = [{'title': "Главная", 'upl_name': "home"},
        {'title': "О нас", 'upl_name': "about"},
        {'title': "Войти", 'upl_name': "login"}
        ]


class homelist(ListView):
    model = Product
    template_name = 'base/home.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'AvtoW'
        context['selected'] = 0
        return context


class showCategory(ListView):
    model = Product
    template_name = 'base/home.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'AvtoW'
        context['selected'] = 0
        return context

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['cat_slag'])


class detailproduct(DetailView):
    model = Product
    template_name = 'base/detailProduct.html'
    pk_url_kwarg = 'product_id'


def about(request):
    return render(request, 'base/about.html', {'menu': menu, 'title': 'О сайте'})


def login(request):
    return render(request, 'base/login.html', {'menu': menu, 'title': 'О сайте'})
