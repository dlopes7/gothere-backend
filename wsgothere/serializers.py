from rest_framework import serializers

from wsgothere.models import Item, Fornecedor, Segmento, Pais, Estado, Cidade, Classe, Bairro, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location


class SegmentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Segmento


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado


class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade


class BairroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bairro


class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
