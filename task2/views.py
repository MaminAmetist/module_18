from django.shortcuts import render

# Create your views here.
def start_func(request):
    return render(request, 'temple_start.html')

def first_func(request):
    return render(request, 'temple_func.html')
