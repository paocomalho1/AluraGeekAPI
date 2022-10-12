from rest_framework import serializers
from alurageek.models import Produtos


class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'
