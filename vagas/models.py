from django.db import models
from django.contrib.auth.models import User


class Curriculo(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    nome = models.CharField(max_length=150)
    arquivo = models.FileField(upload_to="curriculos/")
    texto_extraido = models.TextField(blank=True)
    skills_extraidas = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Vaga(models.Model):
    titulo = models.CharField(max_length=150)
    empresa = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    skills_exigidas = models.TextField()
    salario_estimado = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.empresa}"


class MatchResultado(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    curriculo = models.ForeignKey(Curriculo, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    skills_encontradas = models.TextField(blank=True)
    skills_faltantes = models.TextField(blank=True)
    percentual_match = models.FloatField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.curriculo.nome} x {self.vaga.titulo} - {self.percentual_match}%"
