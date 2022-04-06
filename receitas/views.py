from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Receita

# Create your views here.

def index(request):

    #mostrando todos os objetos presentes no banco
    receitas = Receita.objects.all()
    dados = {
        'receitas' : receitas
    }
    return render(request, 'index.html',dados)

def receita(request, receita_id):

    #pegando chave primaria como argumento
    receita  = get_object_or_404(Receita, pk=receita_id)

    #criar dicionarios para renderizar no template
    receita_a_exibir = {
        'receita' : receita
    }

    #passando o dicionario como argumento
    return render(request, 'receita.html', receita_a_exibir)
