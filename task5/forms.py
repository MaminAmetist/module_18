from django import forms
from django.core.exceptions import ValidationError


def validate_age(value):
    if int(value) < 18:
        raise ValidationError('Вы должны быть старше 18.')
    return value


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин:', error_messages={'required': 'Тысяча чертей!', },
                               help_text='Имя пользователя должно быть не более 30 символовю')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(), label='Введите пароль:',
                               error_messages={'required': 'Пароль слишком короткий.', },
                               help_text='Пароль должен содержать не менее 8 символов.')
    repeat_password = forms.CharField(min_length=8, widget=forms.PasswordInput(), label='Повторите пароль:')
    age = forms.IntegerField(min_value=18, label='Введите свой возраст:',
                             error_messages={'required': 'Вы должны быть старше 18.', })
    # age = forms.IntegerField(label='Введите свой возраст:', validators=[validate_age])
    subscribe = forms.BooleanField(required=False, label='Подписаться на рассылку.')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if ' ' in username:
            raise forms.ValidationError('Имя пользователя не должно содержать пробелы.')
        if len(username) > 30:
            raise forms.ValidationError('Имя пользователя должно быть не более 30 символов.')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        repeat_password = self.cleaned_data.get('repeat_password')
        if password != repeat_password:
            raise forms.ValidationError('Пароли не совпадают.')
        return password

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if len(str(age)) > 3:
            raise forms.ValidationError('Столько не живут.')
