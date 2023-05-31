
# Despatcher
Despatcher do middleware idealizado pela disciplina de programação distribuida no periodo letivo de 2023.1
#
# Arquitetura

![App Screenshot](https://cdn.discordapp.com/attachments/1110264962665943123/1110531478615502848/Captura_de_Tela_2023-05-23_as_08.35.19.png)

## Documentação da API

#### Envia publicação para rede social

```http
  POST /api/publicar
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `api_key` | `string` | **Obrigatório**. Token jwt para autenticação |

Recebe o nome da rede social de destino como parâmetro, assim como os dados a serem publicados.

