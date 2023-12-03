from rest_framework import serializers
from loja.models import *
from loja.serializer import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta :
        model = Cliente
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta :
        model = Produto
        fields = '__all__'

class VendaSerializer(serializers.ModelSerializer):
    class Meta :
        model = Venda
        fields = '__all__'


class ItemVendaSerializer(serializers.ModelSerializer):
    class Meta :
        model = ItemVenda
        fields = '__all__'

class ListaItemVendaSerializer(serializers.ModelSerializer):
    """Listar todos os produtos da venda 1 Vendas/1/Produtos"""
    produto = serializers.ReadOnlyField(source='produto.nome')
    vendedor = serializers.ReadOnlyField(source='vendedor.nome')
    class Meta :
        model = ItemVenda
        fields = '__all__'
    def get_ListaItemVendas(self, obj):
        return obj.get_ListaItemVendas_display()
    
class ListarVendasVendedorSerializer(serializers.ModelSerializer):
    vendedor_nome = serializers.ReadOnlyField(source='vendedor.nome')
    cliente_nome = serializers.ReadOnlyField(source='cliente.nome')
    class Meta :
        model = Venda
        fields = '__all__'
        def get_VendasVendedor(self,obj):
            return obj.get_vendasVendedor_display()