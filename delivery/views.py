from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def user(request, name, age):
    return HttpResponse(f'<h1>Name {name}, age {age}</h1>')


def about(request):
    return HttpResponse("About")


def contact(request):
    return HttpResponseRedirect("/about")


def details(request):
    return HttpResponsePermanentRedirect("/")