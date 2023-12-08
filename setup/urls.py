from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from loja.views import ClientesViewSet, VendaViewSet, ProdutoViewSet, ItemVendaViewSet,ListaItemVendas, ListaVendasVendedorView
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('Clientes',ClientesViewSet, basename= 'Clientes')
router.register('Vendas',VendaViewSet, basename= 'Vendas')
router.register('Produtos',ProdutoViewSet, basename= 'Produtos')
router.register('ItemsVendas',ItemVendaViewSet, basename= 'ItemsVendas')
router.register('vendedor/1/vendas/',ItemVendaViewSet, basename= 'vendedorEVendas')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('venda/<int:pk>/produtos/',ListaItemVendas.as_view()),
    path('vendedor/<int:pk>/vendas/', ListaVendasVendedorView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)