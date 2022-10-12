from rest_framework import viewsets
from alurageek.models import Produtos
from alurageek.serializers import ProdutosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ProdutoViewSet(viewsets.ModelViewSet):
    """Exibindo Todos os Produtos"""
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer
    ordering_fields = ['titulo','preco']
    search_fields = ['titulo']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
