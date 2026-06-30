from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cadastro/", views.cadastro_usuario, name="cadastro_usuario"),
    path("login/", views.login_usuario, name="login_usuario"),
    path("logout/", views.logout_usuario, name="logout_usuario"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("upload/", views.upload_curriculo, name="upload_curriculo"),
    path("curriculos/", views.listar_curriculos, name="listar_curriculos"),
    path("vagas/", views.listar_vagas, name="listar_vagas"),
    path("atualizar-vagas/", views.atualizar_vagas, name="atualizar_vagas"),
    path("resultado/<int:resultado_id>/", views.resultado, name="resultado"),
]
