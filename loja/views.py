from rest_framework import viewsets, generics
from loja.models import Cliente,GrupoProduto,Produto,Vendedor,Venda,ItemVenda
from loja.serializer import VendaSerializer,ClienteSerializer,ProdutoSerializer,ItemVendaSerializer, ListaItemVendaSerializer,ListarVendasVendedorSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    "exibir todos clientes"
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class VendaViewSet(viewsets.ModelViewSet):
    "exibir todAs VENDAS"
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    "exibir todos protudos"
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ItemVendaViewSet(viewsets.ModelViewSet):
    "exibir todos itens em uma venda"
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer

class ListaItemVendas(generics.ListAPIView):
    def get_queryset(self):
      queryset = ItemVenda.objects.filter(venda_id=self.kwargs['pk'])
      return queryset
    serializer_class = ListaItemVendaSerializer

class ListaVendasVendedorView(generics.ListAPIView):
    def get_queryset(self):
        queryset = Venda.objects.filter(vendedor_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListarVendasVendedorSerializer

