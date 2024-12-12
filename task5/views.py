from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.
def sign_up_by_django(request):
    users = ['Anna', 'Den', 'Cat']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            subscribe = form.cleaned_data['subscribe']
            if password == repeat_password and len(str(age)) <= 3 and username not in users:
                return HttpResponse(f'Приветствуем, {username}!')
            elif username in users:
                info['error'] = 'Пользователь уже существует.'
        else:
            form = UserRegister()
    return render(request, 'registration_page_django.html', {'form': form, 'info': info})


def sign_up_by_html(request):
    users = ['Anna', 'Den', 'Cat']
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        subscribe = request.POST.get('subscribe')
        if password == repeat_password and int(age) >= 18 and username not in users:
            return HttpResponse(f'Приветствуем, {username}!')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают.'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18.'
        elif username in users:
            info['error'] = 'Пользователь уже существует.'
    return render(request, 'registration_page_html.html', context=info)
