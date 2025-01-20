from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'pages/index.html')

def sobre(request):
    return HttpResponse('Sobre')

def contato(request):
    return HttpResponse('Contato')

def planos(request):
    return HttpResponse('Planos')