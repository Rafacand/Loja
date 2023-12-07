from django.db import models

class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()
    ativo = models.BooleanField(default= True)
   
    def __str__(self):
        return self.nome
    
class GrupoProduto(models.Model):
    TIPO = (
        ('cozinha','Cozinha'),
        ('sala','Sala'),
        ('banheiro', 'Banheiro'),
    )
    grupo_produto_id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100, choices=TIPO, null=False,default='cozinha')

    def __str__(self):
        return self.tipo

class Produto(models.Model):
    produto_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    grupo_produto = models.ForeignKey(GrupoProduto, on_delete=models.CASCADE, blank= False)

    def __str__(self):
        return self.nome

class Vendedor(models.Model):
    vendedor_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    venda_id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    data_venda = models.DateField()
    total_venda = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.venda_id)

class ItemVenda(models.Model):
    item_id = models.AutoField(primary_key=True)
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
       return str(self.item_id)
