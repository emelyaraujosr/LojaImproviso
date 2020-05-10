# Generated by Django 3.0.6 on 2020-05-09 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='price')),
                ('estoque', models.IntegerField(verbose_name='estoque')),
            ],
        ),
    ]