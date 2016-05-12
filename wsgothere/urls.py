from django.conf.urls import include, url
from rest_framework import routers

from wsgothere.views import SegmentoViewSet, FornecedorViewSet, ItemViewSet, PaisViewSet, EstadoViewSet, CidadeViewSet, \
    ClasseViewSet, BairroViewSet

router = routers.DefaultRouter()
router.register(r'Segmento', SegmentoViewSet, base_name='SegmentoViewSet')
router.register(r'Fornecedor', FornecedorViewSet, base_name='FornecedorViewSet')
router.register(r'Item', ItemViewSet, base_name='ItemViewSet')
router.register(r'Pais', PaisViewSet, base_name='PaisViewSet')
router.register(r'Estado', EstadoViewSet, base_name='EstadoViewSet')
router.register(r'Cidade', CidadeViewSet, base_name='CidadeViewSet')
router.register(r'Classe', ClasseViewSet, base_name='ClasseViewSet')
router.register(r'Bairro', BairroViewSet, base_name='BairroViewSet')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),

]
