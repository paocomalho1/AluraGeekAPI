from django.db import models

class Users(models.Model):

    nome = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, blank=False)
    senha = models.CharField(max_length=13,blank=False)
    admin = models.BooleanField(blank=False, null=False, default=False)

    def __str__(self):
        return self.nome

class Produtos(models.Model):
    CATEGORIA=(
        ("SW","Star Wars"),
        ("C","Console"),
        ("D", "Diversos")    
    )
    user = models.ForeignKey(Users ,on_delete=models.CASCADE, default=1)
    titulo = models.CharField(max_length=30)
    preco = models.FloatField(max_length=10)
    categoria = models.CharField(max_length=3, choices=CATEGORIA, blank=False, null=False, default="D")
    url = models.CharField(max_length=500)
    descricao = models.TextField(max_length=1200)

    def __str__(self):
        return self.titulo
