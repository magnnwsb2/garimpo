from django.contrib import admin
from .models import Curriculo, Vaga, MatchResultado


@admin.register(Curriculo)
class CurriculoAdmin(admin.ModelAdmin):
    list_display = ("nome", "usuario", "skills_extraidas", "criado_em")
    search_fields = ("nome", "skills_extraidas", "usuario__username")


@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "empresa", "skills_exigidas", "salario_estimado", "criada_em")
    search_fields = ("titulo", "empresa", "skills_exigidas")


@admin.register(MatchResultado)
class MatchResultadoAdmin(admin.ModelAdmin):
    list_display = ("curriculo", "vaga", "usuario", "percentual_match", "criado_em")
    search_fields = ("curriculo__nome", "vaga__titulo", "usuario__username")
