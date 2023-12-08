from rest_framework import viewsets, generics, filters
from loja.models import Cliente,GrupoProduto,Produto,Vendedor,Venda,ItemVenda
from loja.serializer import VendaSerializer,ClienteSerializer,ProdutoSerializer,ItemVendaSerializer, ListaItemVendaSerializer,ListarVendasVendedorSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class ClientesViewSet(viewsets.ModelViewSet):
    "exibir todos clientes"
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['cliente_id']
    search_fields = ['nome', 'cpf']
    filterset_fields = ['ativo']
    Http_method_names = ['get', 'post', 'put', 'path']

    @method_decorator(cache_page(20)) #segundos
    def dispatch(self, *args, **kwargs):
        return super(ClientesViewSet,self,).dispatch(*args,**kwargs)

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
    
    @method_decorator(cache_page(20)) #segundos
    def dispatch(self, *args, **kwargs):
        return super(ProdutoViewSet,self,).dispatch(*args,**kwargs)
    

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
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['vendedor_id']
    search_fields = ['vendedor__vendedor_id','data_venda']
    

    def get_queryset(self):
        #tudo que o vendedor x vendeu para todos
        queryset = Venda.objects.filter(vendedor=self.kwargs['pk'])
        return queryset
    serializer_class = ListarVendasVendedorSerializer

    @method_decorator(cache_page(20)) #segundos
    def dispatch(self, *args, **kwargs):
        return super(ListaVendasVendedorView,self,).dispatch(*args,**kwargs)

