from rest_framework import viewsets

from wsgothere.models import Fornecedor, Segmento, Item, Pais, Estado, Cidade, Classe, Bairro, Location
from wsgothere.serializers import SegmentoSerializer, ItemSerializer, FornecedorSerializer, PaisSerializer, \
    EstadoSerializer, CidadeSerializer, ClasseSerializer, BairroSerializer, LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects.all()


class SegmentoViewSet(viewsets.ModelViewSet):
    serializer_class = SegmentoSerializer

    def get_queryset(self):
        return Segmento.objects.all()


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.all()


class FornecedorViewSet(viewsets.ModelViewSet):
    serializer_class = FornecedorSerializer

    def get_queryset(self):
        return Fornecedor.objects.all()


class PaisViewSet(viewsets.ModelViewSet):
    serializer_class = PaisSerializer

    def get_queryset(self):
        return Pais.objects.all()


class EstadoViewSet(viewsets.ModelViewSet):
    serializer_class = EstadoSerializer

    def get_queryset(self):
        return Estado.objects.all()


class CidadeViewSet(viewsets.ModelViewSet):
    serializer_class = CidadeSerializer

    def get_queryset(self):
        return Cidade.objects.all()


class BairroViewSet(viewsets.ModelViewSet):
    serializer_class = BairroSerializer

    def get_queryset(self):
        return Bairro.objects.all()


class ClasseViewSet(viewsets.ModelViewSet):
    serializer_class = ClasseSerializer

    def get_queryset(self):
        return Classe.objects.all()
