from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Franquia(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome

class Franqueada(models.Model):
    nome = models.CharField(max_length=45)
    cnpj = models.CharField(max_length=11)
    franquia = models.ForeignKey(Franquia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class BurguerUser(AbstractUser):
    franquia = models.ForeignKey(Franquia, null = True, on_delete=models.SET_NULL)
    franqueada = models.ForeignKey(Franqueada, null = True, on_delete=models.SET_NULL)


        #... any other fields ...
class Produto(models.Model):
    nome = models.CharField(max_length=45)
    preco = models.FloatField()
    franquia = models.ForeignKey(Franquia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
   id = models.AutoField(primary_key=True) 
   franqueada = models.ForeignKey('Franqueada', on_delete=models.CASCADE)
   produtos = models.ManyToManyField('Produto', through='PedidoProduto', through_fields=('pedido','produto'))
   pago = models.BooleanField()   

   def __str__(self):
      return "Pedido #" + str(self.id)
class PedidoProduto(models.Model):
    pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE)
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    quantidade = models.IntegerField()


class Contrato(models.Model):
    nome = models.CharField(max_length=45)
    descricao = models.CharField(max_length=200)
    valor = models.FloatField()
    franqueada = models.ForeignKey(Franqueada, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome    