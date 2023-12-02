from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from loja.views import ClientesViewSet, VendaViewSet, ProdutoViewSet, ItemVendaViewSet

router = routers.DefaultRouter()
router.register('Clientes',ClientesViewSet, basename= 'Clientes')
router.register('Vendas',VendaViewSet, basename= 'Vendas')
router.register('Produtos',ProdutoViewSet, basename= 'Produtos')
router.register('ItemsVendas',ItemVendaViewSet, basename= 'ItemsVendas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]