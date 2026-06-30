# Garimpo

Garimpo é um MVP acadêmico desenvolvido para a disciplina de Programação Avançada.

O sistema realiza curadoria simples de vagas de emprego, permitindo upload de currículo em PDF, extração básica de skills técnicas, importação de vagas reais via fonte externa e cálculo de compatibilidade entre o perfil do usuário e vagas cadastradas.

## Objetivo

Criar um auditor simples de compatibilidade técnica para vagas de emprego, identificando:

- Skills encontradas no currículo
- Skills exigidas pela vaga
- Skills faltantes
- Percentual de compatibilidade
- Vagas mais aderentes ao perfil do usuário

## Funcionalidades implementadas no MVP

- Interface web em Django
- Menu lateral de navegação
- Upload de currículo em PDF
- Extração simples de texto do currículo com pdfplumber
- Identificação de skills técnicas a partir de uma base pré-definida
- Página para visualizar currículos enviados
- Cadastro de vagas pelo Admin Django
- Carregamento de vagas demo
- Importação de vagas reais por API externa
- Persistência de currículos, vagas e resultados no banco SQLite
- Cálculo de match entre currículo e vaga
- Exibição do resultado diretamente abaixo da vaga
- Botão de detalhes após o cálculo
- Página de detalhes explicando a fórmula do match
- Versionamento com Git/GitHub

## Tecnologias utilizadas

- Python
- Django
- Django REST Framework
- SQLite
- pdfplumber
- requests
- HTML/CSS
- Git/GitHub
- Render

## Arquitetura simplificada

Usuário
↓
Interface Django
↓
Upload de Currículo PDF
↓
Extração de Texto e Skills
↓
Banco SQLite
↓
Importação/Listagem de Vagas
↓
Cálculo de Match
↓
Resultado e Detalhes

## Como executar localmente

1. Clonar o repositório:

    git clone https://github.com/magnnwsb2/garimpo.git
    cd garimpo

2. Criar e ativar ambiente virtual:

    python3 -m venv .venv
    source .venv/bin/activate

3. Instalar dependências:

    pip install -r requirements.txt

4. Executar migrations:

    python manage.py migrate

5. Rodar servidor:

    python manage.py runserver

Acesse:

    http://127.0.0.1:8000/

## Rotas principais

- / : Página inicial
- /upload/ : Upload de currículo PDF
- /curriculos/ : Lista de currículos enviados
- /vagas/ : Lista de vagas e cálculo de match
- /seed-vagas/ : Carrega vagas demo
- /importar-vagas-reais/ : Importa vagas reais por API externa
- /admin/ : Administração Django

## Cálculo de compatibilidade

percentual de match =
(quantidade de skills encontradas / quantidade total de skills exigidas pela vaga) x 100

Exemplo:

Skills da vaga: python, sql, django, docker  
Skills encontradas no currículo: python, sql, docker  

Match = 3 / 4 x 100 = 75%

## Banco de Dados

Nesta versão, o projeto utiliza SQLite para persistência local.

Tabelas principais:

- Curriculo
- Vaga
- MatchResultado

## Docker

Docker não foi utilizado nesta versão MVP.

A decisão foi manter a entrega simples e funcional, usando ambiente virtual Python com venv. Docker está previsto como evolução futura do projeto.

## Deploy

O deploy em nuvem será realizado no Render.

O objetivo é disponibilizar a aplicação com:

- Link público
- Código versionado no GitHub
- Execução em ambiente web
- Persistência básica para demonstração

## Status

MVP funcional em desenvolvimento.

Versão atual: v0.1.0
