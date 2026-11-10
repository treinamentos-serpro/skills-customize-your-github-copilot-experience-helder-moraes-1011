# 📘 Assignment: File Organizer with Python

## 🎯 Objective

Crie um programa de linha de comando que organize arquivos em uma pasta por extensão. Pratique `pathlib`, funções e operações seguras com arquivos usando apenas a biblioteca padrão do Python.

## 📝 Tasks

### 🛠️ Classify Files by Extension

#### Descrição
Complete a função que determina a categoria de um arquivo. Use a extensão em letras minúsculas como nome da pasta e classifique arquivos sem extensão em `no-extension`.

#### Requisitos
O programa concluído deve:

- Retornar a extensão sem o ponto e em letras minúsculas, como `pdf` para `report.PDF`
- Retornar `no-extension` para arquivos sem extensão
- Usar `pathlib.Path` para consultar o caminho do arquivo


### 🛠️ Preview the Organization Plan

#### Descrição
Implemente a função que percorre apenas os arquivos diretamente dentro da pasta informada e monta uma lista de caminhos de origem e destino. Antes de mover qualquer arquivo, mostre ao usuário o plano que será executado.

#### Requisitos
O programa concluído deve:

- Ignorar subpastas e seus conteúdos
- Criar uma pasta de destino para cada categoria de extensão
- Exibir os caminhos de origem e destino sem alterar os arquivos durante a prévia


### 🛠️ Apply the Plan Safely

#### Descrição
Adicione a opção `--apply` para executar o plano. Sem essa opção, o programa deve apenas mostrar a prévia. Ao aplicar o plano, crie as pastas de destino conforme necessário e não substitua arquivos existentes.

#### Requisitos
O programa concluído deve:

- Exibir uma prévia por padrão e mover arquivos somente quando `--apply` for informado
- Pular e informar arquivos cujo destino já exista, sem sobrescrevê-los
- Informar quando o caminho fornecido não for uma pasta válida
- Usar somente módulos da biblioteca padrão do Python