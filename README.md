
# Despatcher
Despatcher do middleware idealizado pela disciplina de programação distribuida no periodo letivo de 2023.1
#
# Arquitetura

![App Screenshot](https://cdn.discordapp.com/attachments/1110264962665943123/1113603134388981910/Middleware_Structure.png)

## Documentação da API

O Despatcher disponibiliza uma API RESTful que permite o acesso aos módulos do sistema.

Recursos disponíveis para acesso via API:

* [**Criar Publicação**](#reference/create)
* [**Deletar Publicação**](#reference/delete)
* [**Modificar Publicação**](#reference/update)


## URLs de acesso
URL local: https://localhost:3060/despatcher

URL web (a definir): https://exemplo.com.br/api


## Métodos
Requisições para a API devem seguir os padrões:
| Método | Descrição |
|---|---|
| `POST` | Utilizado para criar um novo registro. |
| `PUT` | Atualiza dados de um registro ou altera sua situação. |
| `DELETE` | Remove um registro do sistema. |


## Respostas

| Código | Descrição |
|---|---|
| `200` | Requisição executada com sucesso (success).|
| `400` | Erros de validação ou os campos informados não existem no sistema.|
| `404` | Registro pesquisado não encontrado (Not found).|
| `405` | Método não implementado.|
| `422` | Dados informados estão fora do escopo definido para o campo.|
| `500` | Erro de processamento de dados

### Criar publicação [POST /create]

+ Request (application/json)
    + Body

            {
                "usuario":"fulano@teste.com",
                "senha":"senha@1234",
                "idPublicação":"5bd96678-8a9b-4332-919b-50597186eedd",
                "twitter":"true",
                "linkedin":"false",
                "conteudo":"Conteudo em texto da publicação",
                "arquivo": "ZmlsZTovLy9ob21lL2FsdW5vL0RvY3VtZW50b3MvcHljaGFybS1jb21tdW5pdHktMjAyMy4xLjIvYmluL3Jlc3RhcnQucHkK"
            }

+ Response 200 (application/json)

        {
            "message": "Publicação criada com sucesso!"
        }
### Remover publicação [DELETE /delete]

+ Request (application/json)
    + Body

            {
                "usuario":"fulano@teste.com",
                "senha":"senha@1234",
                "idPublicação":"5bd96678-8a9b-4332-919b-50597186eedd",
                "twitter":"true",
                "linkedin":"false",
            }

+ Response 200 (application/json)

        {
            "message": "Publicação excluida com sucesso!"
        }

### Atualizar publicação [PUT /update]

+ Request (application/json)
    + Body

            {
                "usuario":"fulano@teste.com",
                "senha":"senha@1234",
                "idPublicação":"5bd96678-8a9b-4332-919b-50597186eedd",
                "twitter":"true",
                "linkedin":"false",
                "conteudo":"Conteudo em texto da publicação",
                "arquivo": "ZmlsZTovLy9ob21lL2FsdW5vL0RvY3VtZW50b3MvcHljaGFybS1jb21tdW5pdHktMjAyMy4xLjIvYmluL3Jlc3RhcnQucHkK"
            }

+ Response 200 (application/json)

        {
            "message": "Publicação atualizada com sucesso!"
        }
