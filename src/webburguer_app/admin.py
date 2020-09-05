from django.contrib import admin
from .models import BurguerUser, Franquia, Franqueada, Contrato, Produto, PedidoProduto, Pedido
from django.contrib.auth.models import User, Group

admin.site.site_header = "Administração WebBurguer"
admin.site.index_title = "Seja bem-vindo a administração de franquias !"

class PedidoProdutoInline(admin.TabularInline):
    model = PedidoProduto
    extra = 1
class PedidoAdmin(admin.ModelAdmin):
    inlines = (PedidoProdutoInline,)
    
admin.site.unregister(Group)
admin.site.register(BurguerUser)
admin.site.register(Franquia)
admin.site.register(Franqueada)
admin.site.register(Contrato)
admin.site.register(Produto)
admin.site.register(Pedido, PedidoAdmin)