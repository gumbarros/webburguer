from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import get_user_model
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
        return render(request, 'registration/cadastro_franqueado.html', {'franqueadaForm':franqueadaForm, 'userForm':userForm})

@login_required
def home(request):
    return render(request, 'home.html', {'franqueada': request.user.franqueada})

def handler404(request):
    return render(request, '404.html')

def handler500(request):
    return render(request, '505.html')