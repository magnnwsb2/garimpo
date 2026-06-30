from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Curriculo, Vaga, MatchResultado
from .services import (
    extrair_texto_pdf,
    extrair_skills,
    normalizar_lista_skills,
    calcular_match,
    buscar_vagas_remotive,
    limpar_html,
)


def home(request):
    return render(request, "vagas/home.html")


def upload_curriculo(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        arquivo = request.FILES.get("arquivo")

        if not nome or not arquivo:
            return render(request, "vagas/upload.html", {
                "erro": "Informe o nome e selecione um arquivo PDF."
            })

        curriculo = Curriculo.objects.create(
            nome=nome,
            arquivo=arquivo
        )

        texto = extrair_texto_pdf(curriculo.arquivo.path)
        skills = extrair_skills(texto)

        curriculo.texto_extraido = texto
        curriculo.skills_extraidas = ", ".join(skills)
        curriculo.save()

        return redirect("listar_curriculos")

    return render(request, "vagas/upload.html")


def listar_curriculos(request):
    curriculos = Curriculo.objects.all().order_by("-criado_em")

    return render(request, "vagas/curriculos.html", {
        "curriculos": curriculos,
    })


def listar_vagas(request):
    vagas = Vaga.objects.all().order_by("-criada_em")
    curriculos = Curriculo.objects.all().order_by("-criado_em")
    resultado_match = None

    if request.method == "POST":
        vaga_id = request.POST.get("vaga_id")
        curriculo_id = request.POST.get("curriculo_id")

        vaga = get_object_or_404(Vaga, id=vaga_id)
        curriculo = get_object_or_404(Curriculo, id=curriculo_id)

        skills_curriculo = normalizar_lista_skills(curriculo.skills_extraidas)
        skills_vaga = normalizar_lista_skills(vaga.skills_exigidas)

        encontradas, faltantes, percentual = calcular_match(
            skills_curriculo,
            skills_vaga
        )

        resultado_match = MatchResultado.objects.create(
            curriculo=curriculo,
            vaga=vaga,
            skills_encontradas=", ".join(encontradas),
            skills_faltantes=", ".join(faltantes),
            percentual_match=percentual,
        )

    return render(request, "vagas/vagas.html", {
        "vagas": vagas,
        "curriculos": curriculos,
        "resultado_match": resultado_match,
    })


def seed_vagas(request):
    vagas_exemplo = [
        {
            "titulo": "Engenheiro de Dados Júnior",
            "empresa": "Garimpo Tech",
            "descricao": "Atuação com pipelines de dados, banco de dados relacional, scripts Python e apoio na construção de dashboards.",
            "skills_exigidas": "python, sql, postgresql, git, pandas",
            "salario_estimado": 4500.00,
        },
        {
            "titulo": "Desenvolvedor Python Django",
            "empresa": "CodeLab Sistemas",
            "descricao": "Desenvolvimento de aplicações web com Django, APIs REST, banco de dados e versionamento com Git.",
            "skills_exigidas": "python, django, api, rest, sql, git, github",
            "salario_estimado": 5200.00,
        },
        {
            "titulo": "Analista de Dados",
            "empresa": "Data Insight Brasil",
            "descricao": "Análise de dados, criação de relatórios, tratamento de bases e construção de indicadores para áreas de negócio.",
            "skills_exigidas": "sql, excel, power bi, pandas, python",
            "salario_estimado": 4000.00,
        },
    ]

    for vaga in vagas_exemplo:
        Vaga.objects.get_or_create(
            titulo=vaga["titulo"],
            empresa=vaga["empresa"],
            defaults={
                "descricao": vaga["descricao"],
                "skills_exigidas": vaga["skills_exigidas"],
                "salario_estimado": vaga["salario_estimado"],
            }
        )

    messages.success(request, "Vagas demo carregadas com sucesso.")
    return redirect("listar_vagas")


def importar_vagas_reais(request):
    vagas_api = buscar_vagas_remotive()
    total_importadas = 0

    for item in vagas_api[:20]:
        titulo = item.get("title", "Vaga sem título")
        empresa = item.get("company_name", "Empresa não informada")
        descricao = limpar_html(item.get("description", ""))

        texto_para_skills = f"{titulo} {descricao}"
        skills = extrair_skills(texto_para_skills)

        if not skills:
            skills = ["python", "sql"]

        _, criada = Vaga.objects.get_or_create(
            titulo=titulo[:150],
            empresa=empresa[:150],
            defaults={
                "descricao": descricao[:3000],
                "skills_exigidas": ", ".join(skills),
                "salario_estimado": None,
            }
        )

        if criada:
            total_importadas += 1

    messages.success(
        request,
        f"{total_importadas} vagas reais importadas da fonte externa."
    )

    return redirect("listar_vagas")


def resultado(request, resultado_id):
    resultado_match = get_object_or_404(MatchResultado, id=resultado_id)

    return render(request, "vagas/resultado.html", {
        "resultado": resultado_match
    })
