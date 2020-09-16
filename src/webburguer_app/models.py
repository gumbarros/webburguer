from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

ESTADOS = (
    ('ac','AC'),
    ('al','AL'),
    ('ap','AP'),
    ('am','AM'),
    ('ba','BA'),
    ('ce','CE'),
    ('df','DF'),
    ('es','ES'),
    ('go','GO'),
    ('ma','MA'),
    ('mt','MT'),
    ('ms','MS'),
    ('mg','MG'),
    ('pa','PA'),
    ('pb','PB'),
    ('pr','PR'),
    ('pe','PE'),
    ('pi','PI'),
    ('rj','RJ'),
    ('rn','RN'),
    ('rs','RS'),
    ('ro','RO'),
    ('rr','RR'),
    ('sc','SC'),
    ('sp','SP'),
    ('se','SE'),
    ('to','TO')
)

class Endereco(models.Model):
    rua = models.CharField(max_length=25)
    bairro = models.CharField(max_length=25)
    cidade = models.CharField(max_length=25)
    cep = models.CharField(max_length=8)
    uf = models.CharField(max_length=2, choices=ESTADOS, default='sp')

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

class Franqueada(models.Model):
    nome = models.CharField(max_length=45)
    cnpj = models.CharField(max_length=11)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.nome


class BurguerUser(AbstractUser):
    franqueada = models.ForeignKey(Franqueada, null = True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

class Produto(models.Model):
    nome = models.CharField(max_length=45)
    preco = models.FloatField()

    def __str__(self):
        return self.nome

class Pedido(models.Model):
   franqueada = models.ForeignKey('Franqueada', on_delete=models.CASCADE, null=True)
   produto = models.ForeignKey('Produto', on_delete=models.CASCADE, null=True)
   quantidade = models.IntegerField(null=True)
   pago = models.BooleanField(null = True)

   def total(self):
       return (self.produto.preco * self.quantidade)

   def __str__(self):
      return "Pedido #" + str(self.pk)



class Contrato(models.Model):
    nome = models.CharField(max_length=45)
    descricao = models.TextField(max_length=200)
    valor = models.FloatField()
    franqueada = models.ForeignKey(Franqueada, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome