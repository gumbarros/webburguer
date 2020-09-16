from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from .forms import FranqueadaForm, UserForm, PedidoForm
from webburguer_app.models import Franqueada, BurguerUser, Produto, Pedido

def index(request):
    return render(request, 'index.html')

def cadastroFranqueado(request):
    if request.method == "POST":
        franqueadaForm = FranqueadaForm(request.POST)
        userForm = UserForm(request.POST)
        if franqueadaForm.is_valid() and userForm.is_valid():
            franqueada = franqueadaForm.save()
            user = userForm.save()
            user.franqueada = franqueada
            user.save()
            return redirect('/')
    else:
        franqueadaForm = FranqueadaForm()
        userForm = UserForm()
        return render(request, 'registration/cadastro_franqueado.html', {'franqueadaForm':franqueadaForm, 'userForm':userForm})

@login_required
def home(request):
    return render(request, 'home.html', {'franqueada': request.user.franqueada})

@login_required
def cadastroPedido(request):
    if request.method == "POST":
        pedidoForm = PedidoForm(request.POST)
        if pedidoForm.is_valid():
            pedidoForm.franqueada = request.user.franqueada
            pedidoForm.save()
            return redirect('home/')
    else:
        pedidoForm = PedidoForm()
        return render(request, 'cadastro_pedido.html', {'pedidoForm':pedidoForm})

@login_required
def pedidos(request):
    return render(request, 'pedidos.html', {'franqueada': request.user.franqueada})