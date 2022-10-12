from rest_framework import serializers
from alurageek.models import Produtos,Users


class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'



class ProdutosPorUsuarioSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source= "user.nome")
    categoria = serializers.SerializerMethodField()

    class Meta:         
        model= Produtos
        fields = ('id','user','titulo','preco','categoria','url','descricao')
    
    def get_categoria(self, obj):
        return obj.get_categoria_display()
