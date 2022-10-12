from django.contrib import admin
from django.urls import path,include
from alurageek.views import ProdutoViewSet, ProdutosPorUsuario, UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('produtos',ProdutoViewSet, basename="Produtos")
router.register('users',UserViewSet, basename="Users")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("users/<int:pk>/produtos", ProdutosPorUsuario.as_view()),
]
