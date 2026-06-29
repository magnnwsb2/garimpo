# Documento de Requisitos - Projeto Garimpo

## 1. Introdução

O Garimpo é um sistema web de curadoria inteligente de vagas de emprego. Seu objetivo é auxiliar usuários a analisarem a compatibilidade técnica entre seu currículo e vagas cadastradas, identificando skills aderentes e gaps de conhecimento.

## 2. Necessidade do Sistema

Profissionais de tecnologia precisam avaliar rapidamente se uma vaga está alinhada ao seu perfil técnico. A análise manual de requisitos pode ser demorada e imprecisa. O Garimpo automatiza parte desse processo por meio da extração de skills de currículos em PDF e comparação com requisitos de vagas.

## 3. Objetivos

- Permitir upload de currículo em PDF
- Extrair skills técnicas do currículo
- Cadastrar/listar vagas com requisitos técnicos
- Comparar currículo e vaga
- Exibir percentual de compatibilidade
- Identificar skills faltantes

## 4. Estórias de Usuário

### E01 - Upload de Currículo

Como usuário, quero enviar meu currículo em PDF para que o sistema identifique minhas principais skills técnicas.

### E02 - Dashboard de Compatibilidade

Como usuário, quero visualizar o percentual de compatibilidade entre meu currículo e as vagas cadastradas para entender quais oportunidades estão mais alinhadas ao meu perfil.

## 5. Requisitos Funcionais

### RF01 - Upload de Currículo

O sistema deve permitir o envio de um arquivo PDF contendo o currículo do usuário.

### RF02 - Extração de Skills

O sistema deve extrair skills técnicas a partir do texto do currículo.

### RF03 - Listagem de Vagas

O sistema deve permitir visualizar vagas cadastradas com suas respectivas skills exigidas.

### RF04 - Cálculo de Match

O sistema deve calcular o percentual de compatibilidade entre as skills do currículo e as skills exigidas pela vaga.

### RF05 - Exibição de Resultado

O sistema deve exibir skills encontradas, skills faltantes e percentual de compatibilidade.

## 6. Requisitos Não Funcionais

- O sistema deve ser implementado em Django.
- O sistema deve possuir persistência de dados.
- O sistema deve possuir interface web.
- O código deve estar versionado no GitHub.
- A aplicação deve ser publicada no Render.

## 7. Matriz de Rastreabilidade

| RF | Caso de Uso | App | Model | View | Template |
|---|---|---|---|---|---|
| RF01 | Upload de Currículo | vagas | Curriculo | upload_curriculo | upload.html |
| RF02 | Extração de Skills | vagas | Curriculo | extrair_skills | resultado.html |
| RF03 | Listagem de Vagas | vagas | Vaga | listar_vagas | vagas.html |
| RF04 | Cálculo de Match | vagas | MatchResultado | calcular_match | resultado.html |
| RF05 | Exibição de Resultado | vagas | MatchResultado | resultado | resultado.html |

## 8. Links

### Código

https://github.com/magnnwsb2/garimpo

### Projeto em Produção

A definir após deploy no Render.
