import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from loja.models import Cliente,Vendedor,Produto

def criando_pessoas(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name()
        email = '{}@{}'.format(nome.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf.generate()
        endereco = fake.street_address()
        telefone = "{} 9{}-{}".format(random.randrange(10, 21), random.randrange(4000, 9999), random.randrange(4000, 9999))
        ativo = random.choice([True, False])
        p = Cliente(nome=nome, email=email, cpf=cpf, endereco=endereco, telefone=telefone, ativo=ativo)
        p.save()

def criando_vendedores(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(9)
    for _ in range(quantidade_de_pessoas):
        nome = fake.name()
        email = '{}@{}'.format(nome.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        telefone = "{} 9{}-{}".format(random.randrange(10, 21), random.randrange(4000, 9999), random.randrange(4000, 9999))
        p = Vendedor(nome=nome, email=email, telefone=telefone)
        p.save()

def criando_produtos(quantidade_de_produtos):
    Faker.seed(8)
    fake = Faker('pt_BR')
    for _ in range(quantidade_de_produtos):
        nome = fake.language_name()
        descricao =  fake.paragraph(nb_sentences=5)
        preco ="{}.{}".format(random.randrange(1,100),random.randrange(0, 100))
        grupo ="{}".format(random.randrange(1,3))
        p = Produto(nome=nome, descricao=descricao, preco=preco, grupo_produto_id=grupo)
        p.save()


#criando_pessoas(50)
criando_vendedores(10)
#criando_produtos(10)

print('Sucesso!')