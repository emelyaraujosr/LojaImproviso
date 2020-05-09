from django.urls import path
from .views import home, contato, faleConosco, regulamentos, produtos

urlpatterns =[
    path('', home),
    path('contato', contato),
    path('faleConosco',faleConosco),
    path('regulamentos', regulamentos),
    path('produtos', produtos),
]