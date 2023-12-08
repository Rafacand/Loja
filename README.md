
### Projeto visado em comunicação Via API
Estudo sobre api com python e django-rest-framework, aonde temos um banco de dados com as seguintes tabelas 
> Clientes;
> Produtos;
> Grupo de produto;
> Vendedor;
> Vendas(pedido);
> Itens de cada venda efetuada;

Por hora é possível acessar as rotas via aws em uma ec2 com linux(até o dia 10):
- [Clientes](http://3.84.156.158:8000/Clientes/)
- [Vendas](http://3.84.156.158:8000/Vendas/)
- [Produtos](http://3.84.156.158:8000/Produtos/)
- [Itens das Vendas](http://3.84.156.158:8000/ItemsVendas/)
- [Vendas Feito Pelo Vendedor(id)](http://3.84.156.158:8000/vendedor/1/vendas/)
 
<details>
<summary> <b>Como Usar o projeto 08-12-23 </b> </summary>
Instalar : <br>

- Sudo apt install python3.10-venv <br>
ativar a venv <br>

- source venv/bin/activate <br>

Instalar os pacotes utilizando o comando : <br>
- pip install -r requeriments.txt
fazer as migrações
- python manage.py makemigrations
- python manage.py migrate

e se tudo der certo rodar o servidor <br>
- python manage.py runserver

caso precise acessar o admin, criar um via :
python manage.py createsuperuser
</details>

   
É possivel também pesquisar os clientes, por id, nome e cpf <br>
![image](https://github.com/Rafacand/Loja/assets/37985239/9c0ba29a-18d9-4482-802f-60447991fcf2)

Vendas pelo id do Vendedor <br>
![image](https://github.com/Rafacand/Loja/assets/37985239/1032b4e9-ff9b-41cb-be44-7f04eba71dbf)




## Pacotes utilizados
**asgiref==3.7.2:**
   - O pacote `asgiref` fornece uma especificação para a interface entre servidores web e aplicações Python assíncronas. Ele é usado para suportar a execução assíncrona no Django.

**Django==4.2.7:**
   - O Django é um framework web Python de alto nível que incentiva o desenvolvimento rápido e limpo. Ele inclui um ORM (Object-Relational Mapping) para interagir com bancos de dados, um sistema de roteamento, um mecanismo de templates, e muitos outros componentes úteis.

**django-filter==23.5:**
   - O `django-filter` é uma biblioteca que fornece uma maneira fácil de filtrar consultas de objetos do Django. Ele facilita a criação de formulários de filtro em suas visualizações.

**djangorestframework==3.14.0:**
   - O Django REST framework é uma poderosa e flexível toolkit para construir APIs web. Ele é construído sobre a base do Django e simplifica a criação de APIs RESTful.

**Faker==20.1.0:**
   - `Faker` é uma biblioteca que permite gerar dados falsos de maneira realista. É frequentemente usada para criar dados de teste ou preencher um banco de dados com informações fictícias.

**Markdown==3.5.1:**
   - `Markdown` é uma linguagem de marcação leve, muitas vezes usada para formatar texto em páginas da web. O Django REST framework usa essa biblioteca para renderizar descrições de API em Markdown.

**Pillow==10.1.0:**
   - `Pillow` é uma biblioteca de processamento de imagens que estende a biblioteca padrão `PIL` (Python Imaging Library). No contexto do Django, é frequentemente usado para manipular imagens em modelos.

**python-dateutil==2.8.2:**
   - `python-dateutil` fornece funcionalidades para manipulação de datas e horários além do que é oferecido pelo módulo padrão `datetime` do Python.

**pytz==2023.3.post1:**
   - `pytz` é uma biblioteca que lida com fusos horários. No Django, é frequentemente usado para lidar com datas e horas em diferentes fusos horários.

**six==1.16.0:**
    - `six` é uma biblioteca que fornece utilitários para garantir a compatibilidade entre as versões do Python 2 e 3. No entanto, note que essa biblioteca pode não ser mais tão necessária nas versões mais recentes do Django, que são compatíveis apenas com o Python 3.

**sqlparse==0.4.4:**
    - `sqlparse` é uma biblioteca para analisar consultas SQL e formatá-las de maneira legível. Pode ser usado para depurar consultas SQL geradas pelo ORM do Django.

**typing_extensions==4.8.0:**
    - O módulo `typing_extensions` fornece extensões para o módulo `typing` do Python, que é usado para suportar tipos opcionais e anotações de tipo em Python.

**validate-docbr==1.10.0:**
    - `validate-docbr` é uma biblioteca para validação de documentos brasileiros, como CPF e CNPJ. Pode ser útil em aplicativos que lidam com dados pessoais no contexto brasileiro.
