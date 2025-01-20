from django.urls import path
from recipes import views

urlpatterns = [
    path('<int:id>', views.recipe),
    path('contato/', views.contato),
    path('planos/', views.planos),
]
