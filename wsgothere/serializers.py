from rest_framework import serializers
from wsgothere.models import Item, Fornecedor, Segmento, Pais, Estado, Cidade


class SegmentoSerializer(serializers.ModelSerializer):
    segmentos = serializers.HyperlinkedRelatedField(many=True,
                                                    read_only=True,
                                                    view_name='SegmentoViewSet-detail')

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