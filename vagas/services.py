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


TRADUCOES_TECNICAS = {
    "remote": "remoto",
    "job": "vaga",
    "jobs": "vagas",
    "developer": "desenvolvedor",
    "engineer": "engenheiro",
    "data engineer": "engenheiro de dados",
    "software engineer": "engenheiro de software",
    "backend": "back-end",
    "frontend": "front-end",
    "full stack": "full stack",
    "analyst": "analista",
    "data analyst": "analista de dados",
    "scientist": "cientista",
    "data scientist": "cientista de dados",
    "manager": "gerente",
    "product": "produto",
    "team": "equipe",
    "company": "empresa",
    "experience": "experiência",
    "requirements": "requisitos",
    "responsibilities": "responsabilidades",
    "skills": "competências",
    "knowledge": "conhecimento",
    "database": "banco de dados",
    "databases": "bancos de dados",
    "pipeline": "pipeline",
    "pipelines": "pipelines",
    "cloud": "nuvem",
    "application": "aplicação",
    "applications": "aplicações",
    "system": "sistema",
    "systems": "sistemas",
    "development": "desenvolvimento",
    "analytics": "análise de dados",
    "business": "negócio",
    "support": "suporte",
    "customer": "cliente",
    "platform": "plataforma",
    "tools": "ferramentas",
    "work": "trabalho",
    "working": "trabalhando",
    "build": "construir",
    "building": "construção",
    "maintain": "manter",
    "maintaining": "manutenção",
    "design": "projetar",
    "designing": "projeto",
    "create": "criar",
    "creating": "criação",
    "api": "API",
    "apis": "APIs",
    "sql": "SQL",
    "python": "Python",
    "django": "Django",
    "docker": "Docker",
    "git": "Git",
    "github": "GitHub",
    "linux": "Linux",
    "postgresql": "PostgreSQL",
    "mysql": "MySQL",
    "javascript": "JavaScript",
    "typescript": "TypeScript",
    "machine learning": "aprendizado de máquina",
}


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
    """
    if not texto:
        return ""

    texto = re.sub(r"<[^>]+>", " ", texto)
    texto = re.sub(r"&nbsp;", " ", texto)
    texto = re.sub(r"&amp;", "&", texto)
    texto = re.sub(r"\s+", " ", texto)

    return texto.strip()


def traduzir_texto_basico(texto):
    """
    Traduz termos técnicos frequentes para português brasileiro.

    Esta função não substitui um tradutor profissional, mas atende ao MVP
    ao deixar títulos e descrições importados mais compreensíveis.
    """
    if not texto:
        return ""

    texto_traduzido = texto

    for termo_en, termo_pt in sorted(
        TRADUCOES_TECNICAS.items(),
        key=lambda item: len(item[0]),
        reverse=True
    ):
        padrao = re.compile(rf"\b{re.escape(termo_en)}\b", re.IGNORECASE)
        texto_traduzido = padrao.sub(termo_pt, texto_traduzido)

    return texto_traduzido


def traduzir_titulo_vaga(titulo):
    """
    Traduz termos comuns do título da vaga.
    """
    return traduzir_texto_basico(titulo)


def extrair_skills(texto):
    """
    Identifica skills técnicas a partir de uma lista base.
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
    Calcula a compatibilidade técnica entre currículo e vaga.

    Regra:
    - O valor numérico nunca passa de 100.
    - 100 significa que todas as competências da vaga foram atendidas.
    - A interface pode mostrar 100%+ quando o currículo atende tudo
      e ainda possui competências extras.
    """
    if not skills_vaga:
        return [], [], 0

    skills_curriculo_set = set(skills_curriculo)

    encontradas = [
        skill for skill in skills_vaga
        if skill in skills_curriculo_set
    ]

    faltantes = [
        skill for skill in skills_vaga
        if skill not in skills_curriculo_set
    ]

    percentual = round((len(encontradas) / len(skills_vaga)) * 100, 2)

    return encontradas, faltantes, percentual


def buscar_vagas_remotive():
    """
    Busca vagas reais na API pública da Remotive.
    """
    url = "https://remotive.com/api/remote-jobs"
    params = {
        "search": "python data django sql",
        "limit": 30,
    }

    try:
        resposta = requests.get(url, params=params, timeout=15)
        resposta.raise_for_status()
        dados = resposta.json()
    except Exception:
        return []

    return dados.get("jobs", [])
