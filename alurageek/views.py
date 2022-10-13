from rest_framework import viewsets,generics
from alurageek.models import Produtos, Users
from alurageek.serializers import ProdutosPorUsuarioSerializer, ProdutosSerializer, UsersSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ProdutoViewSet(viewsets.ModelViewSet):
    """Exibindo Todos os Produtos"""
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """Exibindo Todos os Usuarios"""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class ProdutosPorUsuario(generics.ListAPIView):
    """Filtrando Produtos por Usuario"""
    def get_queryset(self):
        querySet = Produtos.objects.filter(user=self.kwargs['pk'])
        return querySet
    serializer_class = ProdutosPorUsuarioSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
