from re import search
from rest_framework import viewsets
from alurageek.models import Produtos
from alurageek.serializers import ProdutosSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    """Exibindo Todos os Produtos"""
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer
    ordering_fields = ['titulo','preco']
    search_fields = ['titulo']
