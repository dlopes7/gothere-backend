from django.contrib import admin

# Register your models here.

from wsgothere.models import Segmento, Item, Fornecedor, Pais, Cidade, Estado, Classe

admin.site.register(Segmento)
admin.site.register(Item)
admin.site.register(Fornecedor)
admin.site.register(Pais)
admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Classe)
