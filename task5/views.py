from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.
def sign_up_by_django(request):
    users = ['Anna', 'Den', 'Cat']
    info = []
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            subscribe = form.cleaned_data['subscribe']

    else:
        form = UserRegister()
    return render(request, 'registration_page_django.html', {'form': form})


def sign_up_by_html(request):
    pass
