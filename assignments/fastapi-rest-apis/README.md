# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para administrar um catálogo de livros usando FastAPI. Você praticará rotas HTTP, validação de dados com modelos Pydantic e respostas apropriadas para operações CRUD.

## 📝 Tasks

### 🛠️ Criar a rota para listar livros

#### Descrição
Complete a aplicação FastAPI para iniciar um servidor e disponibilizar uma rota que liste os livros armazenados em memória.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI intitulada `Book Catalog API`
- Instalar as dependências com `python -m pip install fastapi uvicorn`
- Disponibilizar `GET /books` e retornar uma lista JSON, vazia quando não houver livros
- Iniciar com `uvicorn starter-code:app --reload` e exibir a documentação interativa em `/docs`

### 🛠️ Adicionar e consultar livros

#### Descrição
Crie modelos Pydantic para os dados de entrada e saída e implemente operações para adicionar um livro e consultar um livro pelo seu identificador.

#### Requisitos
O programa concluído deve:

- Validar os campos `title` e `author` recebidos no corpo da requisição
- Disponibilizar `POST /books`, atribuir um identificador único e responder com status `201 Created`
- Disponibilizar `GET /books/{book_id}` e retornar o livro solicitado
- Responder com status `404 Not Found` quando o identificador não existir

Exemplo de corpo para criar um livro:

```json
{
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien"
}
```

### 🛠️ Atualizar e remover livros

#### Descrição
Complete as operações CRUD adicionando rotas para substituir os dados de um livro e removê-lo do catálogo.

#### Requisitos
O programa concluído deve:

- Disponibilizar `PUT /books/{book_id}` para atualizar título e autor
- Disponibilizar `DELETE /books/{book_id}` para remover um livro e responder com status `204 No Content`
- Responder com status `404 Not Found` para atualização ou remoção de identificadores inexistentes
- Confirmar cada operação usando `/docs` ou um cliente HTTP e verificar os dados e status retornados