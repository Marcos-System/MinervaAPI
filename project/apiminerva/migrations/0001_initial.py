# Generated by Django 5.0.3 on 2024-03-25 15:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CPF', models.CharField(max_length=11, unique=True)),
                ('nome', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Aviso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_registro', models.DateField(auto_now_add=True)),
                ('mensagem', models.CharField(max_length=500)),
                ('data_para_envio', models.DateField()),
                ('hora_para_envio', models.TimeField()),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avisos', to='apiminerva.pessoa')),
            ],
        ),
    ]
