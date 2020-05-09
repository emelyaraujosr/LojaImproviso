from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def produtos(request):
    return render(request, 'produtos.html')

def contato(request):
    return render(request, 'contato.html')

def faleConosco(request):
    return render(request, 'faleConosco.html')

def regulamentos(request):
    return render(request, 'regulamentos.html')