from django.shortcuts import render
from core.models import Produtos
# Create your views here.

def home(request):
    return render(request, 'home.html')

def produtos(request):
    listaDeProdutos = Produtos.objects.all()
    context = {
        'Produtos': listaDeProdutos
    }
    return render(request, 'produtos.html',context)

def contato(request):
    return render(request, 'contato.html')

def faleConosco(request):
    return render(request, 'faleConosco.html')

def regulamentos(request):
    return render(request, 'regulamentos.html')