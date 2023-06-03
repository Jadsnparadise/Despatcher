from flask import Flask, jsonify, request

import pika

app = Flask(__name__)

@app.route('/')
def hello():
  return 'Olá, Flask!'

@app.route('/pub', methods=['POST'])
def postTest():
  post = request.get_json()
  mensagem = post['pub']['text']
  return publicar(mensagem) 
  

def publicar(mensagem: str): 
  connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
  routing_key = 'create.instagram'
  channel = connection.channel()
  # channel.queue_declare(queue='minha_fila')
  channel.basic_publish(exchange='direct_exchange', routing_key=routing_key, body=mensagem)
  connection.close()
  return f"Mensagem '{mensagem}' enviada em routing_key: {routing_key}"
  
  
if __name__ == '__main__':
    app.run(debug=True)
