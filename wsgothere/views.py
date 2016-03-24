from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render

from rest_framework import viewsets

from wsgothere.serializers import SegmentoSerializer, ItemSerializer, FornecedorSerializer
from wsgothere.models import Fornecedor, Segmento, Item


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