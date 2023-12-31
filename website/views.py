from django.shortcuts import render
from django .http import HttpResponse
from django .template import loader

# Create your views here.
def website(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())
def first(request):
    return render(request, 'first.html')

# class pantai====================================================
def home(request):
    return render(request, 'home.html')
def amed(request):
    return render(request, 'amed.html')
def pandawa(request):
    return render(request, 'pandawa.html')
def melasti(request):
    return render(request, 'melasti.html')
def kuta(request):
    return render(request, 'kuta.html')
def jimbaran(request):
    return render(request, 'jimbaran.html')