from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


from webburguer_app.models import Franquia, Franqueada, BurguerUser, Produto, Pedido, PedidoProduto

def index(request):
    return render(request, 'webburguer_app/home.html')