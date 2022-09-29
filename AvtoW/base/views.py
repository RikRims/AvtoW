from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
#для авторизации
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import RegisterUserForm
from .utils import *
from .models import *


class homelist(DataMixin, ListView):
    model = Product
    template_name = 'base/home.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='AvtoW')
        return dict(list(context.items()) + list(c_def.items()))


class showCategory(DataMixin, ListView):
    model = Product
    template_name = 'base/home.html'
    context_object_name = 'product'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['product'][0].category),
                                      selected=context['product'][0].category)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['cat_slag'])


class detailproduct(DataMixin, DetailView):
    model = Product
    template_name = 'base/detailProduct.html'
    pk_url_kwarg = 'product_id'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['product'])
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'base/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))


def about(request):
    return render(request, 'base/about.html')


def login(request):
    return render(request, 'base/login.html')
