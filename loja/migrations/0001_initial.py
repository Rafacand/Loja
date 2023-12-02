# Generated by Django 4.2.7 on 2023-12-01 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cliente_id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('telefone', models.CharField(max_length=15)),
                ('endereco', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GrupoProduto',
            fields=[
                ('grupo_produto_id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(choices=[('cozinha', 'Cozinha'), ('sala', 'Sala'), ('banheiro', 'Banheiro')], default='cozinha', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('vendedor_id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('venda_id', models.AutoField(primary_key=True, serialize=False)),
                ('data_venda', models.DateField()),
                ('total_venda', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.cliente')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('produto_id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('grupo_produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.grupoproduto')),
            ],
        ),
        migrations.CreateModel(
            name='ItemVenda',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantidade', models.IntegerField()),
                ('preco_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.produto')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.venda')),
            ],
        ),
    ]
