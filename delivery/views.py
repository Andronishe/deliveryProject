from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm
from .models import *


def index(request):
    products = Product.objects.all()
    context = {
        'products': products,
        # 'gs_games': gs_games,
        'title': 'Главная страница',
    }
    return render(request, 'index.html', context=context)

def show_courier(request):
    courier = Courier.objects.all()
    context = {
        'courier': courier,
        'title': 'Курьеры',
    }
    return render(request, 'courier.html', context=context)

@login_required
def favourite_list(request):
    new = Product.objects.filter(favourites=request.user)
    return render(request, 'favourites.html', {"new": new})


@login_required
def favourite_add(request, id):
    product = get_object_or_404(Product, id=id)
    if product.favourites.filter(id=request.user.id).exists():
        product.favourites.remove(request.user)
    else:
        product.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def total_price(request, price):
    count = request.POST.get('count')


def about(request):
    return render(request, 'about.html', { 'title': 'О сайте'})

def courier(request):
    courier = Courier.objects.all()
    context = {
        'products': courier,
        'title': 'Информация о курьерах',
    }
    return render(request, 'courier.html', context=context)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def show_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    fav = bool

    if product.favourites.filter(id=request.user.id).exists():
        fav = True

    context = {
        'product': product,
        'title': product.name,
        'fav': fav,
    }
    return render(request, 'product.html', context=context)

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')