from django import forms
from django.views import generic
from .models import Franqueada, BurguerUser, Pedido, PedidoProduto
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
        self.fields['quantidade'].label = 'Produto'
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = PedidoProduto
        fields = ('produto','quantidade',)

class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Nome de Usuário'
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirmação de Senha'
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
            field.field.help_text = None
    class Meta:
      model = BurguerUser
      fields = ('username', 'password1', 'password2')
