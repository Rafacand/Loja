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
