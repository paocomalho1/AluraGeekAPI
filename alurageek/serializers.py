from rest_framework import serializers
from alurageek.models import Produtos,Users
from alurageek.validators import *

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

    def validate(self,data):
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'Não inclua digitos numericos neste campo'})
        if not senha_valida(data['senha']):
            raise serializers.ValidationError({'senha':'O campo senha deve conter no minimo 6 digitos'})
        return data

class ProdutosPorUsuarioSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source= "user.nome")
    categoria = serializers.SerializerMethodField()

    class Meta:         
        model= Produtos
        fields = ('id','user','titulo','preco','categoria')
    
    def get_categoria(self, obj):
        return obj.get_categoria_display()