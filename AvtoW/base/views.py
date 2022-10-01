from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from .form import RegisterUserForm
from .utils import *
from .models import *

menu = [{'title': "Мои заказы", 'upl_name': "orderlist"},
        {'title': "О нас", 'upl_name': "about"},
        {'title': "Регистрация", 'upl_name': "login"}]


class homelist(DataMixin, ListView):
    model = Product
    template_name = 'base/home.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='AvtoW')
        return dict(list(context.items()) + list(c_def.items()))


class orderlist(LoginRequiredMixin, DataMixin, ListView):
    model = Order
    template_name = 'base/orders.html'
    context_object_name = 'orders'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Мои заказы')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Order.objects.filter(client=self.request.user)


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
    slug_url_kwarg = 'product_id'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['product'])
        return dict(list(context.items()) + list(c_def.items()))


def detailorders(request, order_id):
    orders = Order.objects.filter(pk=order_id)
    order_items = Order_Item.objects.all()
    cats = Category.objects.annotate(Count('product'))
    return render(request, 'base/detailorders.html', {'orders': orders, 'order_items': order_items, 'menu': menu, 'cats': cats})


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'base/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def about(request):
    return render(request, 'base/about.html')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'base/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
