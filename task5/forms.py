from django import forms
from django.core.exceptions import ValidationError


def validate_age(value):
    if int(value) < 18:
        raise ValidationError('Вы должны быть старше 18.')


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин:')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(), label='Введите пароль:')
    repeat_password = forms.CharField(min_length=8, widget=forms.PasswordInput(), label='Повторите пароль:')
    age = forms.IntegerField(min_value=18, label='Введите свой возраст:', validators=[validate_age], required='Вы должны быть старше 18.')
    # age = forms.IntegerField(label='Введите свой возраст:', validators=[validate_age])
    subscribe = forms.BooleanField(required=False, label='Подписаться на рассылку.')
