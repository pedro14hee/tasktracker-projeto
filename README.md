# TaskTracker

Aplicação de linha de comando (CLI) em Python 3 para organizar tarefas de forma simples e estruturada.
Projeto do **Bootcamp II** (CEUB) — Fase 2: Entrega Intermediária.

**Autor:** Pedro Henrique Alves dos Santos — Ciência de Dados e Machine Learning

## Problema

Sem um sistema centralizado, é comum esquecer prazos, perder o foco por falta de priorização e retrabalhar.
O TaskTracker centraliza o cadastro e a visualização das tarefas.

## Funcionalidades

- Cadastrar tarefas com título, descrição, prioridade e data limite
- Visualizar todas as tarefas cadastradas (ID, título, descrição, prioridade, data limite e status)
- Menu interativo contínuo até o usuário escolher sair

## Regras de negócio

- **Título obrigatório:** entradas vazias ou só com espaços são rejeitadas e o prompt se repete
- **Prioridade restrita:** aceita apenas `Alta`, `Média` (ou `Media`) e `Baixa`
- **Status inicial:** toda tarefa nasce como `Pendente`
- **ID único:** numérico e sequencial

## Tecnologias

- Python 3.8+ (somente biblioteca padrão)
- Git e GitHub

## Como executar

```bash
git clone https://github.com/pedro14hee/tasktracker-projeto.git
cd tasktracker-projeto
python src/main.py
```

## Estrutura do repositório

```
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Próximos passos (Fase 3)

Empacotamento, containerização com Docker, testes e deploy.
