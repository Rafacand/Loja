# Generated by Django 4.2.7 on 2023-12-03 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_alter_cliente_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(default='0', max_length=11, unique=True),
        ),
    ]