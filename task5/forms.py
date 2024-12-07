from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин:')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(), label='Введите пароль:')
    repeat_password = forms.CharField(min_length=8, widget=forms.PasswordInput(), label='Повторите пароль:')
    # age = forms.IntegerField(max_value=100, min_value=18, label='Введите свой возраст:')
    age = forms.IntegerField(label='Введите свой возраст:')
    subscribe = forms.BooleanField(required=False, label='Подписаться на рассылку.')
