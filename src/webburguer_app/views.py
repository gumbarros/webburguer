from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from webburguer_app.models import Franqueada, BurguerUser, Produto, Pedido, PedidoProduto

def index(request):
    return render(request, 'index.html')