from django.shortcuts import render


# Create your views here.
def started_func(request):
    text_1 = 'Главная страница'
    context = {'text_1': text_1, }
    return render(request, 'temple_start.html', context)


def store_func(request):
    head_list = 'Список доступных товаров:'
    games = ["Atomic Heart", "Cyberpunk 2077", "PayDay 2"]
    context = {'head_list': head_list,
               'games': games, }
    return render(request, 'temple_store.html', context)


def buy_func(request):
    text_head = 'Денег нет, но вы держитесь'
    context = {'text_head': text_head, }
    return render(request, 'temple_buy.html', context)
