from rest_framework import serializers
from loja.models import *
from loja.serializer import *
from loja.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta :
        model = Cliente
        fields = '__all__'
    def validate(self,data):
        if not valida_cpf(data['cpf']):
              raise serializers.ValidationError({"cpf":"O CPF deve Conter exatamente 11 digitos"})
        if not valida_nome(data['nome']):
              raise serializers.ValidationError({"nome":"O Nome deve somente letras"})
        return data

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta :
        model = Produto
        fields = '__all__'
    def validate(self,data):
        if valida_preco(data['preco']):
            raise serializers.ValidationError({"preco":"Valor menor que 0"})
        return data

class VendaSerializer(serializers.ModelSerializer):
    class Meta :
        model = Venda
        fields = '__all__'
    def validate(self,data):
        if valida_venda(data['total_venda']):
            raise serializers.ValidationError({"total_venda":"Valor menor que 0"})
        return data


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