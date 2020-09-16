from django.urls import path, include
import django.contrib.auth
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/cadastro_franqueado/', views.cadastroFranqueado),
    path('home/', views.home),
    path('pedidos/', views.pedidos),
    path('cadastro_pedido/', views.cadastroPedido),
    path('pagar_pedido/<int:id>/', views.pagarPedido),
    path('contratos/', views.contratos),
    path('cadastro_contrato', views.cadastroContrato),
    path('produtos/', views.produtos),
    path('cadastro_produto', views.cadastroProduto)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)