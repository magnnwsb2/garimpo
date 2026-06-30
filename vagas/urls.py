from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("upload/", views.upload_curriculo, name="upload_curriculo"),
    path("curriculos/", views.listar_curriculos, name="listar_curriculos"),
    path("vagas/", views.listar_vagas, name="listar_vagas"),
    path("seed-vagas/", views.seed_vagas, name="seed_vagas"),
    path("importar-vagas-reais/", views.importar_vagas_reais, name="importar_vagas_reais"),
    path("resultado/<int:resultado_id>/", views.resultado, name="resultado"),
]
