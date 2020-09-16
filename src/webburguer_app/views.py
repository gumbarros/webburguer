from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from .forms import FranqueadaForm, UserForm, PedidoForm, ContratoForm, ProdutoForm
from webburguer_app.models import Franqueada, BurguerUser, Produto, Pedido, Contrato
from django.conf.urls.static import static

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
    return render(request, 'home.html', {
        'franqueada': request.user.franqueada,
        'pedidos':Pedido.objects.all().filter(franqueada=request.user.franqueada).count(),
        'produtos': Produto.objects.all().count(),
        'contratos': Contrato.objects.all().count()
        })

@login_required
def cadastroPedido(request):
    if request.method == "POST":
        pedidoForm = PedidoForm(request.POST)
        if pedidoForm.is_valid():
            pedido = pedidoForm.save()
            pedido.pago = False
            pedido.franqueada = request.user.franqueada
            pedido.save()
            return redirect('/pedidos/')
    else:
        pedidoForm = PedidoForm()
        return render(request, 'cadastro_pedido.html', {'pedidoForm':pedidoForm})

@login_required
def cadastroProduto(request):
    if request.method == "POST":
        produtoForm = ProdutoForm(request.POST, request.FILES)
        print(produtoForm.errors)
        if produtoForm.is_valid():
            produtoForm.save()
            return redirect('/produtos/')
        else:
            return redirect('/produtos/')  
    else:
        produtoForm = ProdutoForm()
        return render(request, 'cadastro_produto.html', {'produtoForm':produtoForm})

@login_required
def cadastroContrato(request):
    if request.method == "POST":
        contratoForm = ContratoForm(request.POST)
        if contratoForm.is_valid():
            contrato = contratoForm.save()
            contrato.franqueada = request.user.franqueada
            contrato.save()
            return redirect('/contratos/')
    else:
        contratoForm = ContratoForm()
        return render(request, 'cadastro_contrato.html', {'contratoForm':contratoForm})

@login_required
def pagarPedido(request, id):
    pedido = Pedido.objects.get(id=id)
    pedido.pago = True
    pedido.save()
    return redirect('/pedidos/')

@login_required
def pedidos(request):
    return render(request, 'pedidos.html', {'pedidos': Pedido.objects.all().filter(franqueada=request.user.franqueada)})

@login_required
def produtos(request):
    return render(request, 'produtos.html', {'produtos': Produto.objects.all()})

@login_required
def contratos(request):
    return render(request, 'contratos.html', {'contratos': Contrato.objects.all().filter(franqueada=request.user.franqueada)})