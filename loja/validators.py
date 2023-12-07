""" Validacoes Cliente"""

def valida_cpf(cpf):
    return len(cpf) == 11

def valida_nome(nome):
    return nome.isalpha()

""" Validacoes Produtos"""
def valida_preco(preco):
    return preco <= 0

"""Validacoes Vendas"""
def valida_venda(total_venda):
    return total_venda <= 0

        