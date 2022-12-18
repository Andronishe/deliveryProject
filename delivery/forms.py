from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class CountForm(forms.Form):
    address = forms.CharField(label="Введите адрес")
    phone = forms.CharField(label="Введите свой телефон")

class ProductsFilter(forms.Form):
    min_price = forms.DecimalField(label='от', required=False)
    max_price = forms.DecimalField(label='до', required=False)
    ordering = forms.ChoiceField(label='сортировка', required=False, choices=[
        ['name', 'по алфавиту'],
        ['-name', 'по антиалфавиту'],
        ['-price', 'по убыванию цены'],
        ['price', 'по возрастанию цены']
    ])

