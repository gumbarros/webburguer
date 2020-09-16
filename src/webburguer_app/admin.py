from django.contrib import admin
from .models import BurguerUser, Endereco, Franqueada, Contrato, Produto, Pedido
from django.contrib.auth.models import User, Group

admin.site.site_header = "Administração WebBurguer"
admin.site.index_title = "Seja bem-vindo a administração de franquias !"

admin.site.unregister(Group)
admin.site.register(BurguerUser)
admin.site.register(Endereco)
admin.site.register(Franqueada)
admin.site.register(Contrato)
admin.site.register(Produto)
admin.site.register(Pedido)