from django.contrib import admin
from django.urls import path,include
from alurageek.views import ProdutoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('produtos',ProdutoViewSet, basename="Produtos")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
