# Generated by Django 4.1.3 on 2022-11-19 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_carrinho_valortotal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinho',
            name='valorTotal',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
