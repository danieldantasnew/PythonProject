from django.urls import path
from recipes import views

app_name = 'recipes'

urlpatterns = [

    path('', views.home, name='home'),
    path('recipes/<int:id>', views.recipe, name='recipes'),
    path('contato/', views.contato, name='contato'),
    path('planos/', views.planos, name='planos'),
]
