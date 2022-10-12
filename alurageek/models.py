from django.db import models

class Produtos(models.Model):
    CATEGORIA=(
        ("SW","Star Wars"),
        ("C","Console"),
        ("D", "Diversos")    
    )
    titulo = models.CharField(max_length=30)
    preco = models.FloatField(max_length=10)
    categoria = models.CharField(max_length=3, choices=CATEGORIA, blank=False, null=False, default="D")
    url = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500)

    def __str__(self):
        return self.titulo
