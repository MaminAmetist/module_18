from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def start_func(request):
    return render(request, 'temple_start.html')

def first_func(request):
    return render(request, 'temple_func.html')

class first_class(TemplateView):
    template_name = 'temple_class.html'