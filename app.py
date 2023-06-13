from flask import Flask, jsonify, request
import pika

app = Flask(__name__)

#Método POST
@app.route('/pub/create', methods=['POST'])
def createPost():
  post = request.get_json()
  mensagem = post['pub']['text']
  perfil = post['pub']['userId']
  return create(mensagem, perfil) 
  
#Método PUT
@app.route('/pub/update', methods=['PUT'])
def updatePost():
  post = request.get_json()
  mensagem = post['pub']['text']
  return update(mensagem) 

#Método DELETE
@app.route('/pub/delete', methods=['DELETE'])
def deletePost():
  post = request.get_json()
  mensagem = post['pub']['text']
  pubId = post['pub']['pubId']
  return delete(mensagem, pubId) 

#Envia uma mensagem para o rabbitmq para criar um post de acordo com a id do usuário
def create(mensagem: str, userid: str): 
  connection = pika.BlockingConnection(pika.ConnectionParameters('localhost')) 
  channel = connection.channel()
  routing_key = defineRoutingKey("create")
  channel.queue_declare(queue=defineQueue("create"))
  channel.basic_publish(exchange='direct_exchange', routing_key=routing_key, body=mensagem)
  connection.close()
  return f"Mensagem '{mensagem}' enviada em routing_key: {routing_key} para criar um post no perfil: {userid}"

#Envia uma mensagem para o rabbitmq para atualizar um post de acordo com a id da publicação
def update(mensagem: str, pubId: str): 
  connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
  channel = connection.channel()
  routing_key = defineRoutingKey("update")
  channel.queue_declare(queue=defineQueue("update"))
  channel.basic_publish(exchange='direct_exchange', 
                        routing_key=routing_key, 
                        body=mensagem)
  connection.close()
  return f"Mensagem '{mensagem}' foi atualizada na publicação: {pubId} usando a routing_key: {routing_key} "

#Envia uma mensagem para o rabbitmq para deletar um post de acordo com a id da publicação
def delete(mensagem: str, pubId: str): 
  connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
  channel = connection.channel()
  routing_key = defineRoutingKey("delete")
  channel.queue_declare(queue=defineQueue("delete"))
  channel.basic_publish(exchange='direct_exchange',
                        routing_key=routing_key, 
                        body=mensagem)
  connection.close()
  return f"a mensagem:'{mensagem}' foi deletada em routing_key: {routing_key} para a publicação: {pubId}"

#Define a routing key da mensagem que será enviada de acordo com o método HTTP chamado
def defineRoutingKey(method: str):
  post = request.get_json()
  routing_key = method + '.' + post['pub']['socialMedia']['socialMediaId']
  return routing_key

#Define a fila a qual a mensagem será enviada de acordo com o método HTTP chamado
def defineQueue(method: str):
  post = request.get_json()
  queue = method.lower() + '_' + post['pub']['socialMedia']['socialMediaId'] + '_post'
  return queue

  
if __name__ == '__main__':
    app.run(debug=True)
