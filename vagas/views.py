from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import never_cache

from .models import Curriculo, MatchResultado, Vaga
from .services import (
    buscar_vagas_remotive,
    calcular_match,
    extrair_skills,
    extrair_texto_pdf,
    limpar_html,
    normalizar_lista_skills,
    traduzir_texto_basico,
    traduzir_titulo_vaga,
)


def filtrar_curriculos_por_usuario(request):
    if request.user.is_authenticated:
        return Curriculo.objects.filter(usuario=request.user).order_by("-criado_em")

    return Curriculo.objects.filter(usuario__isnull=True).order_by("-criado_em")


def filtrar_matches_por_usuario(request):
    if request.user.is_authenticated:
        return MatchResultado.objects.filter(usuario=request.user).order_by("-criado_em")

    return MatchResultado.objects.filter(usuario__isnull=True).order_by("-criado_em")


def filtrar_vagas_por_busca(request):
    termo = request.GET.get("q", "").strip()

    vagas = Vaga.objects.all()

    if termo:
        vagas = vagas.filter(
            Q(titulo__icontains=termo)
            | Q(empresa__icontains=termo)
            | Q(descricao__icontains=termo)
            | Q(skills_exigidas__icontains=termo)
        )

    return vagas.order_by("-criada_em"), termo


@never_cache
def home(request):
    return render(request, "vagas/home.html")


@never_cache
def cadastro_usuario(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("dashboard")
    else:
        form = UserCreationForm()

    return render(request, "vagas/cadastro.html", {"form": form})


@never_cache
def login_usuario(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect("dashboard")
    else:
        form = AuthenticationForm()

    return render(request, "vagas/login.html", {"form": form})


@never_cache
def logout_usuario(request):
    logout(request)
    response = redirect("home")
    response["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response["Pragma"] = "no-cache"
    response["Expires"] = "0"
    return response


@never_cache
def dashboard(request):
    curriculos = filtrar_curriculos_por_usuario(request)
    vagas, filtro_vagas = filtrar_vagas_por_busca(request)
    matches = filtrar_matches_por_usuario(request)

    curriculo_selecionado = None
    vaga_selecionada = None
    resultado_vaga_selecionada = None
    ranking_vagas = []

    curriculo_id = request.GET.get("curriculo_id")
    vaga_id = request.GET.get("vaga_id")

    if curriculo_id:
        curriculo_selecionado = get_object_or_404(curriculos, id=curriculo_id)
    elif curriculos.exists():
        curriculo_selecionado = curriculos.first()

    if vaga_id:
        vaga_selecionada = get_object_or_404(Vaga, id=vaga_id)

    if curriculo_selecionado:
        skills_curriculo = normalizar_lista_skills(
            curriculo_selecionado.skills_extraidas
        )
        skills_curriculo_set = set(skills_curriculo)

        for vaga in vagas:
            skills_vaga = normalizar_lista_skills(vaga.skills_exigidas)
            skills_vaga_set = set(skills_vaga)

            encontradas, faltantes, percentual = calcular_match(
                skills_curriculo,
                skills_vaga
            )

            excede_requisitos = (
                percentual == 100
                and not faltantes
                and len(skills_curriculo_set - skills_vaga_set) > 0
            )

            indice_label = "100%+" if excede_requisitos else f"{percentual}%"

            if percentual >= 100:
                classe_indice = "score-cyan"
            elif percentual >= 70:
                classe_indice = "score-green"
            elif percentual >= 40:
                classe_indice = "score-yellow"
            else:
                classe_indice = "score-red"

            item = {
                "vaga": vaga,
                "percentual": percentual,
                "indice_label": indice_label,
                "classe_indice": classe_indice,
                "excede_requisitos": excede_requisitos,
                "encontradas": encontradas,
                "faltantes": faltantes,
            }

            ranking_vagas.append(item)

            if vaga_selecionada and vaga.id == vaga_selecionada.id:
                resultado_vaga_selecionada = item

        ranking_vagas = sorted(
            ranking_vagas,
            key=lambda item: item["percentual"],
            reverse=True
        )

        if not resultado_vaga_selecionada and ranking_vagas:
            resultado_vaga_selecionada = ranking_vagas[0]
            vaga_selecionada = resultado_vaga_selecionada["vaga"]

    contexto = {
        "curriculos": curriculos,
        "vagas": vagas,
        "matches": matches,
        "curriculo_selecionado": curriculo_selecionado,
        "vaga_selecionada": vaga_selecionada,
        "resultado_vaga_selecionada": resultado_vaga_selecionada,
        "ranking_vagas": ranking_vagas,
        "total_curriculos": curriculos.count(),
        "total_vagas": vagas.count(),
        "total_matches": matches.count(),
        "filtro_vagas": filtro_vagas,
    }

    return render(request, "vagas/dashboard.html", contexto)


@never_cache
def upload_curriculo(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        arquivo = request.FILES.get("arquivo")

        if not nome or not arquivo:
            messages.error(request, "Informe o nome e selecione um currículo em PDF.")
            return redirect("upload_curriculo")

        curriculo = Curriculo.objects.create(
            nome=nome,
            arquivo=arquivo,
            usuario=request.user if request.user.is_authenticated else None,
        )

        texto = extrair_texto_pdf(curriculo.arquivo.path)
        skills = extrair_skills(texto)

        curriculo.texto_extraido = texto
        curriculo.skills_extraidas = ", ".join(skills)
        curriculo.save()

        messages.success(request, "Currículo enviado e processado com sucesso.")
        return redirect("listar_curriculos")

    return render(request, "vagas/upload.html")


@never_cache
def listar_curriculos(request):
    curriculos = filtrar_curriculos_por_usuario(request)

    return render(
        request,
        "vagas/curriculos.html",
        {"curriculos": curriculos},
    )


@never_cache
def listar_vagas(request):
    vagas, filtro_vagas = filtrar_vagas_por_busca(request)
    curriculos = filtrar_curriculos_por_usuario(request)
    resultado_match = None

    if request.method == "POST":
        vaga_id = request.POST.get("vaga_id")
        curriculo_id = request.POST.get("curriculo_id")

        vaga = get_object_or_404(Vaga, id=vaga_id)
        curriculo = get_object_or_404(curriculos, id=curriculo_id)

        skills_curriculo = normalizar_lista_skills(curriculo.skills_extraidas)
        skills_vaga = normalizar_lista_skills(vaga.skills_exigidas)

        encontradas, faltantes, percentual = calcular_match(
            skills_curriculo,
            skills_vaga
        )

        resultado_match = MatchResultado.objects.create(
            usuario=request.user if request.user.is_authenticated else None,
            curriculo=curriculo,
            vaga=vaga,
            skills_encontradas=", ".join(encontradas),
            skills_faltantes=", ".join(faltantes),
            percentual_match=percentual,
        )

        messages.success(request, "Match calculado com sucesso.")

    return render(
        request,
        "vagas/vagas.html",
        {
            "vagas": vagas,
            "curriculos": curriculos,
            "resultado_match": resultado_match,
            "filtro_vagas": filtro_vagas,
        },
    )


@never_cache
def atualizar_vagas(request):
    vagas_api = buscar_vagas_remotive()

    novas = 0
    atualizadas = 0

    for item in vagas_api[:30]:
        titulo_original = item.get("title", "Vaga sem título")
        titulo = traduzir_titulo_vaga(titulo_original)

        empresa = item.get("company_name", "Empresa não informada")

        descricao_original = limpar_html(item.get("description", ""))
        descricao = traduzir_texto_basico(descricao_original)

        skills = extrair_skills(
            f"{titulo_original} {descricao_original} {item.get('tags', '')}"
        )

        if not skills:
            skills = ["python", "sql"]

        vaga, criada = Vaga.objects.update_or_create(
            titulo=titulo,
            empresa=empresa,
            defaults={
                "descricao": descricao,
                "skills_exigidas": ", ".join(skills),
                "salario_estimado": None,
            },
        )

        if criada:
            novas += 1
        else:
            atualizadas += 1

    messages.success(
        request,
        f"Vagas atualizadas. Novas: {novas}. Atualizadas: {atualizadas}."
    )

    return redirect("listar_vagas")


@never_cache
def resultado(request, resultado_id):
    match = get_object_or_404(MatchResultado, id=resultado_id)

    if request.user.is_authenticated:
        if match.usuario != request.user:
            return redirect("dashboard")

    return render(request, "vagas/resultado.html", {"resultado": match})
