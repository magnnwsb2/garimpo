# Documento de Requisitos - Projeto Garimpo

## 1. Identificação

Projeto: Garimpo  
Aluno: Magnnws Brunno  
Disciplina: Programação Avançada  
Versão: MVP v0.1  

## 2. Introdução

O Garimpo é um sistema web de curadoria inteligente de vagas de emprego. Seu objetivo é auxiliar usuários a analisarem a compatibilidade técnica entre seu currículo e vagas cadastradas ou importadas de uma fonte externa.

O sistema permite o envio de currículo em PDF, extração básica de skills técnicas, importação de vagas reais e cálculo de compatibilidade entre o perfil do usuário e as oportunidades disponíveis.

## 3. Necessidade do Sistema

Profissionais de tecnologia precisam avaliar rapidamente se uma vaga está alinhada ao seu perfil técnico. A análise manual de requisitos pode ser demorada, repetitiva e imprecisa.

O Garimpo automatiza parte desse processo, permitindo que o usuário envie seu currículo e visualize o percentual de compatibilidade com vagas cadastradas ou importadas.

## 4. Objetivos do Sistema

- Permitir upload de currículo em PDF
- Extrair texto do currículo
- Identificar skills técnicas no currículo
- Listar currículos processados
- Cadastrar vagas pelo painel administrativo
- Carregar vagas de demonstração
- Importar vagas reais por fonte externa
- Persistir currículos, vagas e resultados no banco de dados
- Calcular percentual de compatibilidade entre currículo e vaga
- Exibir competências alinhadas
- Exibir competências faltantes
- Explicar como o cálculo foi realizado

## 5. Painel MVP

O MVP implementado contempla:

- Tela inicial
- Menu lateral
- Tela de upload de currículo
- Tela de currículos enviados
- Tela de vagas cadastradas
- Ação para carregar vagas demo
- Ação para importar vagas reais
- Resultado de match exibido abaixo da vaga
- Página de detalhes do cálculo
- Painel Admin Django

## 6. Estórias de Usuário

### E01 - Upload de Currículo

Como usuário, quero enviar meu currículo em PDF para que o sistema identifique minhas principais skills técnicas.

### E02 - Visualização de Currículos

Como usuário, quero visualizar os currículos enviados para confirmar se o arquivo foi salvo e se as skills foram extraídas corretamente.

### E03 - Consulta de Vagas

Como usuário, quero visualizar vagas cadastradas ou importadas para comparar meu perfil com oportunidades disponíveis.

### E04 - Cálculo de Compatibilidade

Como usuário, quero calcular o percentual de compatibilidade entre meu currículo e uma vaga para entender se a oportunidade é aderente ao meu perfil.

### E05 - Detalhamento do Match

Como usuário, quero visualizar os detalhes do cálculo para entender quais competências estão alinhadas e quais estão faltando.

## 7. Requisitos Funcionais

- RF01: O sistema deve permitir o envio de currículo em PDF.
- RF02: O sistema deve extrair texto do currículo enviado.
- RF03: O sistema deve identificar skills técnicas a partir do currículo.
- RF04: O sistema deve listar os currículos enviados.
- RF05: O sistema deve permitir cadastro de vagas pelo Admin Django.
- RF06: O sistema deve permitir carregar vagas demo.
- RF07: O sistema deve importar vagas reais por fonte externa.
- RF08: O sistema deve listar vagas cadastradas ou importadas.
- RF09: O sistema deve calcular o percentual de compatibilidade entre currículo e vaga.
- RF10: O sistema deve exibir o resultado do match abaixo da vaga.
- RF11: O sistema deve disponibilizar uma página de detalhes do cálculo.

## 8. Requisitos Não Funcionais

- O sistema deve ser implementado em Django.
- O sistema deve possuir persistência de dados.
- O sistema deve possuir interface web.
- O sistema deve utilizar modularização entre models, views, templates e services.
- O sistema deve possuir tratamento básico de exceções na leitura de PDFs e importação externa.
- O código deve estar versionado no GitHub.
- A aplicação deve ser publicada no Render.
- A versão MVP deve priorizar simplicidade e funcionalidade.

## 9. Persistência

A persistência é feita com SQLite na versão MVP.

Entidades persistidas:

- Curriculo
- Vaga
- MatchResultado

## 10. Classes de Projeto

### Curriculo

Responsável por armazenar os dados do currículo enviado, incluindo nome, arquivo PDF, texto extraído e skills identificadas.

### Vaga

Responsável por representar uma oportunidade de emprego, incluindo título, empresa, descrição, skills exigidas e salário estimado.

### MatchResultado

Responsável por armazenar o resultado da comparação entre um currículo e uma vaga, incluindo skills encontradas, skills faltantes e percentual de match.

## 11. Estruturas de Dados Utilizadas

### Lista de Skills

Utilizada para armazenar a base de competências técnicas procuradas nos currículos e nas vagas.

Motivo da escolha: é simples, direta e suficiente para o MVP.

### Strings separadas por vírgula

Utilizadas para armazenar as skills extraídas e exigidas.

Motivo da escolha: reduz complexidade no banco para a versão inicial e facilita a visualização no Admin Django.

### Dicionários

Utilizados no carregamento de vagas demo e no processamento de dados vindos da fonte externa.

Motivo da escolha: representam bem dados estruturados de vagas.

## 12. Tratamento de Exceções

O sistema possui tratamento básico de exceções em pontos críticos:

- Leitura de PDF: caso o arquivo seja inválido ou ilegível, o sistema evita quebrar a aplicação.
- Importação de vagas reais: caso a fonte externa esteja indisponível, o sistema retorna uma lista vazia e mantém o funcionamento da aplicação.

## 13. Fórmula de Match

percentual de match =
(quantidade de skills encontradas / quantidade total de skills exigidas pela vaga) x 100

Exemplo:

Skills exigidas pela vaga: python, sql, django, docker  
Skills encontradas no currículo: python, sql, docker  

Percentual: 3 / 4 x 100 = 75%

## 14. Matriz de Rastreabilidade

| RF | Caso de Uso | App | Model | View | Template |
|---|---|---|---|---|---|
| RF01 | Upload de Currículo | vagas | Curriculo | upload_curriculo | upload.html |
| RF02 | Extração de Texto | vagas | Curriculo | upload_curriculo | upload.html |
| RF03 | Extração de Skills | vagas | Curriculo | upload_curriculo | curriculos.html |
| RF04 | Visualização de Currículos | vagas | Curriculo | listar_curriculos | curriculos.html |
| RF05 | Cadastro de Vagas | vagas | Vaga | Admin Django | admin |
| RF06 | Carregamento de Vagas Demo | vagas | Vaga | seed_vagas | vagas.html |
| RF07 | Importação de Vagas Reais | vagas | Vaga | importar_vagas_reais | vagas.html |
| RF08 | Listagem de Vagas | vagas | Vaga | listar_vagas | vagas.html |
| RF09 | Cálculo de Match | vagas | MatchResultado | listar_vagas | vagas.html |
| RF10 | Resultado Inline | vagas | MatchResultado | listar_vagas | vagas.html |
| RF11 | Detalhes do Cálculo | vagas | MatchResultado | resultado | resultado.html |

## 15. Rotas do Sistema

| Rota | Função |
|---|---|
| / | Página inicial |
| /upload/ | Upload de currículo |
| /curriculos/ | Lista currículos enviados |
| /vagas/ | Lista vagas e calcula match |
| /seed-vagas/ | Carrega vagas demo |
| /importar-vagas-reais/ | Importa vagas reais |
| /resultado/<id>/ | Detalhes do cálculo |
| /admin/ | Painel administrativo Django |

## 16. Link para o Código

https://github.com/magnnwsb2/garimpo

## 17. Link para o Projeto em Produção

A definir após deploy no Render.

## 18. Observação sobre Docker

Docker não foi utilizado nesta versão MVP.

A decisão foi priorizar a entrega funcional no prazo, utilizando ambiente virtual Python com venv. Docker está previsto para uma versão futura do projeto.
