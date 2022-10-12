from rest_framework import viewsets ,generics,filters
from alurageek.models import Produtos,Users
from alurageek.serializers import ProdutosSerializer,UsersSerializer,ProdutosPorUsuarioSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


class ProdutoViewSet(viewsets.ModelViewSet):
    """Exibindo Todos os Produtos"""
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['titulo','preco']
    search_fields = ['titulo']

class UserViewSet(viewsets.ModelViewSet):
    """Exibindo Todos os Usuarios"""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome']
    filterset_fields = ['admin']

class ProdutosPorUsuario(generics.ListAPIView):
    """Filtrando Produtos por Usuario"""
    def get_queryset(self):
        querySet = Produtos.objects.filter(user=self.kwargs['pk'])
        return querySet
    serializer_class = ProdutosPorUsuarioSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]