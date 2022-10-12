from django.contrib import admin
from alurageek.models import Produtos,Users


class ProdutosAdmin(admin.ModelAdmin):
    list_display = ("id","titulo","preco","categoria","url","descricao")
    list_display_links = ('titulo',)
    search_fields = ('titulo',)
    list_per_page= 10
    ordering = ('titulo',)

admin.site.register(Produtos,ProdutosAdmin)


class UsersAdmin(admin.ModelAdmin):
    list_display = ("id","nome","email","senha","admin")
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page= 10
admin.site.register(Users,UsersAdmin)