from rest_framework.test import APITestCase
from loja.models import Cliente,Vendedor,Produto
from rest_framework import status
from django.urls import reverse

class ClienteTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Clientes-list')
        self.cliente_1 = Cliente.objects.create(
            cliente_id='1000',
            nome='Sr Teste',
            cpf='40258023090',
            email='teste@teste.com',
            telefone='123421412',
            endereco='rua testulia',
            ativo=False,
            foto=''
        )
        self.cliente_2 = Cliente.objects.create(
            cliente_id='1001',
            nome='Sra teste 2',
            cpf='97271957090',
            email='teste@teste.com',
            telefone='123421412',
            endereco='rua testulia',
            ativo=True,
            foto=''
        )

        def teste_lista_clientes(self):
            response =self.client.get(self.list_url)
            self.assertEquals(response.status_code,status.HTTP_200_OK)

    def teste_criar_cliente(self):
        data = {  
            'nome':'Srateste',
            'cpf':'57693503005',
            'email':'antôniocaldeira@ig.com.br',
            'telefone':'15 95054-8598',
            'endereco':'Condomínio Nogueira, 1',
            'ativo':True,
            'foto':''
        } 
        response = self.client.post(self.list_url,data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
