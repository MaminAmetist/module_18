from django.shortcuts import render


# Create your views here.
def started_func(request):
    text_1 = 'Главная страница'
    text_2 = 'Главная'
    context = {'text_1': text_1, 'text_2': text_2, }
    return render(request, 'temple_start.html', context)


def store_func(request):
    text_head = 'Радуемся вашему присутствию)'
    head_list = 'Список доступных товаров:'
    text_1 = 'Товар пупупу'
    text_2 = 'Второй товар'
    text_3 = 'И это третий'
    context = {'text_head': text_head,
               'head_list': head_list,
               'text_1': text_1,
               'text_2': text_2,
               'text_3': text_3, }
    return render(request, 'temple_store.html', context)


def buy_func(request):
    text_head = 'Денег нет, но вы держитесь'
    context = {'text_head': text_head, }
    return render(request, 'temple_buy.html', context)
