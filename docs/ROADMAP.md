# Roadmap do Projeto Garimpo

## Versão atual: MVP v0.1

O objetivo desta versão é entregar um produto mínimo viável, funcional, simples e demonstrável para a disciplina de Programação Avançada.

A prioridade do MVP é cumprir os requisitos acadêmicos com uma aplicação real, versionada no GitHub e preparada para publicação no Render.

## Escopo implementado

- Projeto Django criado
- Ambiente virtual Python com venv
- Banco SQLite configurado
- App vagas criado
- Models principais implementados
- Admin Django configurado
- Upload de currículo PDF
- Extração de texto com pdfplumber
- Extração simples de skills técnicas
- Listagem de currículos enviados
- Cadastro de vagas pelo Admin Django
- Atualização de vagas reais
- Importação de vagas reais via API externa
- Persistência das vagas no banco
- Cálculo de compatibilidade entre currículo e vaga
- Resultado exibido abaixo da própria vaga
- Botão de detalhes após o cálculo
- Página de detalhes explicando o cálculo
- Menu lateral de navegação
- Git inicializado
- Repositório GitHub configurado
- Commits enviados para o GitHub

## Escopo ainda necessário para entrega final

- Finalizar testes manuais
- Atualizar documento final de requisitos
- Fazer commit das últimas alterações
- Publicar no Render
- Atualizar link de produção no documento
- Tirar prints para apresentação
- Revisar matriz de rastreabilidade

## Fora do escopo da versão 0.1

- Docker
- Airflow
- Redis
- Celery
- Machine Learning avançado
- Scraping complexo de sites com login
- Login completo de usuários
- CI/CD avançado
- PostgreSQL obrigatório
- Dashboard analítico avançado

## Justificativa do MVP

O projeto foi simplificado para priorizar uma entrega funcional no prazo.

Em vez de implementar uma arquitetura complexa com Docker, Airflow, ML avançado e scraping pesado, a versão 0.1 foca nos requisitos essenciais:

- Persistência
- Classes
- Estruturas de dados
- Modularização
- Tratamento de exceções
- Interface
- Dois casos de uso principais
- Versionamento
- Deploy em nuvem

## Casos de uso implementados

### UC01 - Upload de Currículo

O usuário envia um currículo em PDF. O sistema extrai o texto do arquivo, identifica skills técnicas e salva o currículo no banco de dados.

### UC02 - Calcular Compatibilidade

O usuário seleciona um currículo e uma vaga. O sistema compara as skills extraídas do currículo com as skills exigidas pela vaga e calcula o percentual de match.

### UC03 - Atualizar Vagas

O sistema consulta uma fonte externa de vagas reais, extrai informações básicas e salva as vagas no banco de dados.

## Fluxo do MVP

1. Usuário acessa o Garimpo
2. Usuário envia um currículo em PDF
3. Sistema extrai skills do currículo
4. Sistema salva o currículo no banco
5. Usuário atualiza vagas reais
6. Sistema salva as vagas no banco
7. Usuário acessa a lista de vagas
8. Usuário escolhe um currículo
9. Sistema calcula o match
10. Sistema exibe o resultado abaixo da vaga
11. Usuário pode abrir os detalhes do cálculo

## Roadmap futuro

### Versão 0.2

- Deploy final no Render
- Melhorar interface visual
- Melhorar normalização de skills
- Adicionar filtros de vagas
- Adicionar página de histórico de matches

### Versão 0.3

- PostgreSQL em nuvem
- Melhorar persistência de arquivos
- Adicionar autenticação de usuário
- Separar currículos por usuário

### Versão 0.4

- Docker
- Docker Compose
- Ambiente reproduzível completo

### Versão 1.0

- Dashboard analítico
- Recomendação inteligente de vagas
- NLP mais avançado
- Auditoria salarial
- Relatórios
