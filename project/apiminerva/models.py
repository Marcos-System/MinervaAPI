from django.db import models

class Pessoa(models.Model):
    CPF = models.CharField(max_length=11, unique=True, null=False)
    nome = models.CharField(max_length=70, null=False)
    email = models.EmailField(unique=True, null=False)
    senha = models.CharField(max_length=20, null=False)

class Aviso(models.Model):
    data_registro = models.DateField(auto_now_add=True)
    mensagem = models.CharField(max_length=500, null=False)
    data_para_envio = models.DateField(auto_now_add=False)
    hora_para_envio = models.TimeField(auto_now_add=False)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='avisos')
