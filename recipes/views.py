from django.shortcuts import render
import requests

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    url = 'https://api-receitas-pi.vercel.app/receitas/todas'
    response = requests.get(url)
    receitas = response.json()
    context = {'receitas': receitas,
               'button_is_visible': True,
               }

    return render(request, 'pages/index.html', context)

def recipe(request, id):
    url = f'https://api-receitas-pi.vercel.app/receitas/{id}'
    response = requests.get(url)
    receitas = response.json()
    context = {'receita': receitas,
               'button_is_visible': False
               }
    return render(request, 'pages/recipeIndividual.html', context)

def sobre(request):
    return HttpResponse('Sobre')

def contato(request):
    return HttpResponse('Contato')

def planos(request):
    return HttpResponse('Planos')