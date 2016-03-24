from rest_framework import serializers
from wsgothere.models import Item, Fornecedor, Segmento

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