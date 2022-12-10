from django import template
from delivery.models import *
register = template.Library()



@register.simple_tag()
def get_menu():
    menu = [{'title': "Главная страница", 'url_name': 'home'},
            {'title': "О сайте", 'url_name': 'about'},
            # {'title': "избранное", 'url_name': 'favourite_list'},
            {'title': "Курьеры", 'url_name': 'courier'},
            ]
    return menu
