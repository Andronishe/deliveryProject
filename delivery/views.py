import random

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import RegisterUserForm, CountForm, ProductsFilter
from .models import *


def index(request):
    products = Product.objects.all()
    form = ProductsFilter(request.GET)
    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data["min_price"]).distinct()
            print(products)

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data["max_price"]).distinct()

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])
    context = {
        'products': products,
        "form": form,
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

def create_delivery(request):
    if request.method == "POST":
        courier = Courier.objects.get(id=2)
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        context = {
            'courier': courier.name,
            'courier_phone': courier.telephone,
            'title': 'Подробности доставки',
            'address': address,
            'phone': phone,
        }
        return render(request, 'detail.html', context=context)
    else:
        userform = CountForm()
        return render(request, "delivery.html", {"form": userform})

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


class Search(ListView):
    model = Product
    template_name = "index.html"
    context_object_name = 'products'

    def get_queryset(self):
        product = Product.objects.filter(name__icontains=self.request.GET.get('search'))
        return product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Поиск'
        return context

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')