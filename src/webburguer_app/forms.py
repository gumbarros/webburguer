from django import forms
from django.views import generic
from .models import Franqueada, BurguerUser, Pedido, Produto, Contrato
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


class FranqueadaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FranqueadaForm, self).__init__(*args, **kwargs)
        self.fields['nome'].label = 'Nome da Franqueada'
        self.fields['cnpj'].label = 'CNPJ'
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Franqueada
        fields = ('nome', 'cnpj')


class PedidoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PedidoForm, self).__init__(*args, **kwargs)
        self.fields['produto'].label = 'Produto'
        self.fields['quantidade'].label = 'Quantidade'
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Pedido
        fields = ('produto','quantidade')

class ContratoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContratoForm, self).__init__(*args, **kwargs)
        self.fields['nome'].label = 'Nome'
        self.fields['descricao'].label = 'Descrição'
        self.fields['valor'].label = 'Valor (R$)'
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Contrato
        fields = ('nome','descricao','valor')

class ProdutoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        self.fields['nome'].label = 'Nome'
        self.fields['preco'].label = 'Preço'
        self.fields['imagem'].label = 'Imagem'
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Produto
        fields = ('nome','preco', 'imagem')

class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Nome de Usuário'
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirmação de Senha'
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
            field.field.help_text = None
    class Meta:
      model = BurguerUser
      fields = ('username', 'password1', 'password2')
