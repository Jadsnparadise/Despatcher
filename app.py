from flask import Flask, request
from enum import Enum
import pika


class SocialMedia(Enum):
    TWITTER = "twitter"


app = Flask(__name__)


# Método POST
@app.route("/api/create", methods=["POST"])
def createPost():
    try:
        params = request.get_json()
        validateCreateUpdateJson(params)

        for socialMedia in SocialMedia:
            if socialMedia.value in params:
                create(params, socialMedia.value)

        return "Mensagem enviada para o RabbitMQ"
    except ValueError as e:
        return "Erro:" + str(e)


# Método PUT
@app.route("/api/update", methods=["PUT"])
def updatePost():
    try:
        params = request.get_json()
        validateCreateUpdateJson(params)

        for socialMedia in SocialMedia:
            if socialMedia.value in params:
                update(params, params["idPublicação"], socialMedia.value)

        return "Mensagem enviada para o RabbitMQ"
    except ValueError as e:
        return "Erro:" + str(e)


# Método DELETE
@app.route("/api/delete", methods=["DELETE"])
def deletePost():
    try:
        params = request.get_json()
        validateDeleteJson(params)

        for socialMedia in SocialMedia:
            if socialMedia.value in params:
                delete(params, params["idPublicação"], socialMedia.value)

        return "Mensagem enviada para o RabbitMQ"
    except ValueError as e:
        return "Erro:" + str(e)


# Envia uma mensagem para o rabbitmq para criar um post de acordo com a id do usuário
def create(params: dict, routing: str):
    mensagem = params["conteudo"]
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    routing_key = "create." + routing
    channel.queue_declare(queue="create")
    channel.basic_publish(
        exchange="direct_exchange", routing_key=routing_key, body=mensagem
    )
    connection.close()
    return f"Mensagem '{mensagem}' enviada em routing_key: {routing_key} para criar um post no perfil: {params['userId']}"


# Envia uma mensagem para o rabbitmq para atualizar um post de acordo com a id da publicação
def update(params: dict, pubId: str, routing: str):
    mensagem = params["conteudo"]
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    routing_key = "update." + routing
    channel.queue_declare(queue="update")
    channel.basic_publish(
        exchange="direct_exchange", routing_key=routing_key, body=mensagem
    )
    connection.close()
    return f"Mensagem '{mensagem}' foi atualizada na publicação: {pubId} usando a routing_key: {routing_key} no perfil: {params['userId']}"


# Envia uma mensagem para o rabbitmq para deletar um post de acordo com a id da publicação
def delete(params: dict, pubId: str, routing: str):
    mensagem = params["conteudo"]
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    routing_key = "delete" + routing
    channel.queue_declare(queue="delete")
    channel.basic_publish(
        exchange="direct_exchange", routing_key=routing_key, body=mensagem
    )
    connection.close()
    return f"a mensagem:'{mensagem}' foi deletada em routing_key: {routing_key} para a publicação: {pubId}"


# Validação do JSON de create e update
def validateCreateUpdateJson(json_data):
    expected_attributes = [
        "userId",
        "idPublicação",
        "conteudo",
    ]
    missing_attributes = []

    for attribute in expected_attributes:
        if attribute not in json_data:
            missing_attributes.append(attribute)

    if missing_attributes:
        error_message = "Os seguintes atributos estão faltando no JSON: {}".format(
            ", ".join(missing_attributes)
        )
        raise ValueError(error_message)

    return json_data


# Validação do JSON de delete
def validateDeleteJson(json_data):
    expected_attributes = [
        "userId",
        "idPublicação",
    ]
    missing_attributes = []

    for attribute in expected_attributes:
        if attribute not in json_data:
            missing_attributes.append(attribute)

    if missing_attributes:
        error_message = "Os seguintes atributos estão faltando no JSON: {}".format(
            ", ".join(missing_attributes)
        )
        raise ValueError(error_message)

    return json_data


if __name__ == "__main__":
    app.run(debug=True)
