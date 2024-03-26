from rest_framework import serializers
from apiminerva.models import Pessoa
from apiminerva.models import Aviso

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id','CPF', 'nome', 'email', 'senha']
        
class AvisoSerializer(serializers.ModelSerializer):
    pessoa = serializers.PrimaryKeyRelatedField(queryset=Pessoa.objects.all())

    class Meta:
        model = Aviso
        fields = ['id','data_registro', 'mensagem', 'data_para_envio', 'hora_para_envio', 'pessoa']