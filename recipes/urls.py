from django.urls import path
from recipes.views import home, contato, planos

urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('planos/', planos),
]
