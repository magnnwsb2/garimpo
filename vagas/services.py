import pdfplumber
import requests
import re


SKILLS_BASE = [
    "python",
    "django",
    "sql",
    "postgresql",
    "mysql",
    "docker",
    "git",
    "github",
    "api",
    "rest",
    "pandas",
    "numpy",
    "linux",
    "html",
    "css",
    "javascript",
    "typescript",
    "machine learning",
    "scikit-learn",
    "power bi",
    "excel",
    "aws",
    "azure",
    "gcp",
    "airflow",
    "spark",
    "etl",
    "data engineering",
    "data engineer",
    "analytics",
    "bi",
]


def extrair_texto_pdf(caminho_pdf):
    """
    Extrai texto de um arquivo PDF usando pdfplumber.

    A exceção é tratada retornando uma string vazia para evitar quebra
    da aplicação caso o PDF esteja ilegível ou inválido.
    """
    texto = ""

    try:
        with pdfplumber.open(caminho_pdf) as pdf:
            for pagina in pdf.pages:
                texto += pagina.extract_text() or ""
                texto += "\n"
    except Exception:
        return ""

    return texto


def limpar_html(texto):
    """
    Remove tags HTML simples vindas da API de vagas.

    Essa função mantém o MVP leve, evitando dependências extras.
    """
    if not texto:
        return ""

    texto = re.sub(r"<[^>]+>", " ", texto)
    texto = re.sub(r"\s+", " ", texto)

    return texto.strip()


def extrair_skills(texto):
    """
    Identifica skills técnicas a partir de uma lista base.

    A estrutura escolhida é uma lista simples, pois atende ao MVP e permite
    comparação direta entre currículo e vaga.
    """
    texto_lower = texto.lower()
    encontradas = []

    for skill in SKILLS_BASE:
        if skill in texto_lower:
            encontradas.append(skill)

    return encontradas


def normalizar_lista_skills(texto_skills):
    """
    Converte uma string separada por vírgulas em uma lista normalizada.
    """
    if not texto_skills:
        return []

    return [
        skill.strip().lower()
        for skill in texto_skills.split(",")
        if skill.strip()
    ]


def calcular_match(skills_curriculo, skills_vaga):
    """
    Calcula o percentual de compatibilidade entre currículo e vaga.

    O cálculo considera quantas skills exigidas pela vaga foram encontradas
    no currículo.
    """
    if not skills_vaga:
        return [], [], 0

    encontradas = [
        skill for skill in skills_vaga
        if skill in skills_curriculo
    ]

    faltantes = [
        skill for skill in skills_vaga
        if skill not in skills_curriculo
    ]

    percentual = round((len(encontradas) / len(skills_vaga)) * 100, 2)

    return encontradas, faltantes, percentual


def buscar_vagas_remotive():
    """
    Busca vagas reais na API pública da Remotive.

    Para o MVP, usamos uma fonte externa simples e pública para demonstrar
    ingestão de dados reais e persistência no banco.
    """
    url = "https://remotive.com/api/remote-jobs"
    params = {
        "search": "python data django sql",
        "limit": 20,
    }

    try:
        resposta = requests.get(url, params=params, timeout=15)
        resposta.raise_for_status()
        dados = resposta.json()
    except Exception:
        return []

    return dados.get("jobs", [])
