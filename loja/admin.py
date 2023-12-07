from django.contrib import admin

from loja.models import Cliente,GrupoProduto,Produto,Vendedor,Venda,ItemVenda

class Clientes(admin.ModelAdmin): 
    list_display= ('cliente_id','nome', 'email', 'ativo')
    list_display_links = ('cliente_id', 'nome')
    search_fields = ('nome', 'email',)
    list_per_page = 10
    list_editable = ('ativo',)
    ordering = ('nome',)

admin.site.register(Cliente,Clientes)

class GrupoProdutos(admin.ModelAdmin): 
    list_display= ('grupo_produto_id','tipo')
    list_display_links = ('grupo_produto_id', 'tipo')
    search_fields = ('tipo',)
    list_per_page = 10

admin.site.register(GrupoProduto,GrupoProdutos)

class Produtos(admin.ModelAdmin): 
    list_display= ('produto_id','nome', 'grupo_produto')
    list_display_links = ('produto_id', 'nome')
    search_fields = ('nome', 'grupo_produto',)
    list_per_page = 10
admin.site.register(Produto,Produtos)

class Vendedores(admin.ModelAdmin): 
    list_display= ('vendedor_id','nome', 'email')
    list_display_links = ('vendedor_id', 'nome')
    search_fields = ('nome', 'telefone', 'email')
    list_per_page = 10

admin.site.register(Vendedor,Vendedores)

class Vendas(admin.ModelAdmin): 
    list_display= ('venda_id', 'cliente', 'vendedor', 'total_venda')
    list_display_links = ('venda_id', 'cliente', 'vendedor', 'total_venda')
    search_fields = ('venda_id', 'cliente', 'vendedor', 'total_venda',)
    list_per_page = 10

admin.site.register(Venda,Vendas)

class ItemsVendas(admin.ModelAdmin): 
    list_display= ('item_id','venda', 'produto', 'quantidade')
    list_display_links = ('item_id','venda', 'produto', 'quantidade')
    search_fields = ('item_id','venda', 'produto', 'quantidade',)
    list_per_page = 10

admin.site.register(ItemVenda,ItemsVendas)