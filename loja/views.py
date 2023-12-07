from rest_framework import viewsets, generics, filters
from loja.models import Cliente,GrupoProduto,Produto,Vendedor,Venda,ItemVenda
from loja.serializer import VendaSerializer,ClienteSerializer,ProdutoSerializer,ItemVendaSerializer, ListaItemVendaSerializer,ListarVendasVendedorSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ClientesViewSet(viewsets.ModelViewSet):
    "exibir todos clientes"
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    filterset_fields = ['ativo']

class VendaViewSet(viewsets.ModelViewSet):
    "exibir todAs VENDAS"
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    ordering_fields = ['id']
    

class ProdutoViewSet(viewsets.ModelViewSet):
    "exibir todos protudos"
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    

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

