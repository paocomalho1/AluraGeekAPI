from rest_framework import viewsets
from alurageek.models import Produtos, Users
from alurageek.serializers import ProdutosSerializer, UsersSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ProdutoViewSet(viewsets.ModelViewSet):
    """Exibindo Todos os Produtos"""
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """Exibindo Todos os Usuarios"""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
