# Generated by Django 4.2.7 on 2023-12-08 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0006_alter_cliente_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]