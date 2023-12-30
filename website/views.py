from django.shortcuts import render
from django .http import HttpResponse
from django .template import loader

# Create your views here.
def website(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())
def first(request):
    return render(request, 'first.html')
def home(request):
    return render(request, 'home.html')