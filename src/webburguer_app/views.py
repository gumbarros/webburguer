from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from .forms import FranqueadaForm, UserForm
from webburguer_app.models import Franqueada, BurguerUser, Produto, Pedido, PedidoProduto

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
        return render(request, 'cadastro_franqueado.html', {'franqueadaForm':franqueadaForm, 'userForm':userForm})    