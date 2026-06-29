# Garimpo

Garimpo é um MVP acadêmico desenvolvido para a disciplina de Programação Avançada.

O sistema realiza curadoria simples de vagas de emprego, permitindo upload de currículo em PDF, extração básica de skills técnicas e cálculo de compatibilidade entre o perfil do usuário e vagas cadastradas.

## Objetivo

Criar um auditor simples de compatibilidade técnica para vagas de emprego, identificando:

- Skills encontradas no currículo
- Skills exigidas pela vaga
- Skills faltantes
- Percentual de compatibilidade

## Funcionalidades do MVP

- Upload de currículo em PDF
- Extração simples de texto do currículo
- Identificação de skills técnicas
- Cadastro/listagem de vagas
- Cálculo de match entre currículo e vaga
- Interface web simples em Django
- Deploy em nuvem via Render

## Tecnologias

- Python
- Django
- SQLite
- pdfplumber
- Bootstrap
- Git/GitHub
- Render

## Como executar localmente

```bash
git clone https://github.com/magnnwsb2/garimpo.git
cd garimpo

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
Agora cole este segundo bloco:

```bash
cat > docs/ROADMAP.md <<'EOF'
# Roadmap do Projeto Garimpo

## MVP v0.1

O objetivo desta versão é entregar um produto mínimo viável, funcional e publicado em nuvem.

## Escopo incluído

- Projeto Django
- Banco SQLite
- Upload de currículo PDF
- Extração simples de skills
- Cadastro/listagem de vagas
- Cálculo de compatibilidade
- Página de resultado
- GitHub
- Deploy no Render

## Fora do escopo nesta versão

- Machine Learning avançado
- Scraping automático
- Airflow
- Docker
- Redis
- Celery
- CI/CD avançado
- Login completo

## Casos de uso

### UC01 - Upload de Currículo

O usuário envia um currículo em PDF e o sistema extrai skills técnicas básicas.

### UC02 - Calcular Compatibilidade

O sistema compara as skills extraídas do currículo com as skills exigidas pelas vagas cadastradas e retorna um percentual de match.

## Entregas

- Código no GitHub
- Aplicação publicada no Render
- Documento de requisitos
- Diagramas UML
- Matriz de rastreabilidade
