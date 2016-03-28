from django.db import models
from django.utils import timezone
import datetime as dt

#created by david.lopes

class Segmento(models.Model):
    nome = models.CharField(max_length=200)
    data_criacao = models.DateTimeField(auto_now=True)
    data_edicao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{id} - {nome}'.format(id=self.id, nome=self.nome)

class Pais(models.Model):
    class Meta:
        verbose_name_plural = "Países"
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=3)

    def __str__(self):
        return '{nome} ({sigla})'.format(nome=self.nome, sigla=self.sigla)

class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)
    pais = models.ForeignKey(Pais, related_name='estado_pais')

    def __str__(self):
        return '{nome} ({sigla}) - {pais}'.format(nome=self.nome, sigla=self.sigla, pais=self.pais.nome)


class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    pais = models.ForeignKey(Pais, related_name='pais')
    estado = models.ForeignKey(Estado, related_name='cidade_estado')

    def __str__(self):
        return '{nome} - {estado} - {pais}'.format(nome=self.nome, estado=self.estado.nome, pais=self.pais.nome)

class Fornecedor(models.Model):
    class Meta:
        verbose_name_plural = "Fornecedores"

    segmento = models.ManyToManyField(Segmento, related_name='fornecedor_segmentos')

    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=1000)
    preco_medio = models.FloatField()

    cidade = models.ForeignKey(Cidade, related_name='fornecedor_cidade')
    estado = models.ForeignKey(Estado, related_name='fornecedor_estado')
    pais = models.ForeignKey(Pais, related_name='fornecedor_pais')

    telefone_1 = models.CharField(max_length=20)
    telefone_2 = models.CharField(max_length=20)

    cnpj = models.CharField(max_length=30)


    data_criacao = models.DateTimeField(auto_now=True)
    data_edicao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{id} - {nome}: R${preco}'.format(id=self.id,
                                                 nome=self.nome,
                                                 preco=self.preco_medio)



class Item(models.Model):
    class Meta:
        verbose_name_plural = "Itens"
    produto = models.CharField(max_length=100)
    descricao = models.CharField(max_length=1000)
    valor_unitario = models.FloatField()
    fornecedor = models.ForeignKey(Fornecedor, related_name='fornecedor')
    data_criacao = models.DateTimeField(auto_now=True)
    data_edicao = models.DateTimeField(auto_now_add=True)
    data_vigencia = models.DateTimeField()

    def __str__(self):
        return '{id} - {nome}'.format(id=self.id, nome=self.produto)



