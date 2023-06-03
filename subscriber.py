import pika

# Função de callback para lidar com as mensagens recebidas
def callback(ch, method, properties, body):
    print("Mensagem recebida:", body)

# Estabelece a conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declara a fila
channel.queue_declare(queue='minha_fila')

# Declarando exchange
channel.exchange_declare(
    exchange='direct_exchange',
    exchange_type='direct'
)

# Bind de fila 
channel.queue_bind(
  exchange="direct_exchange",
  queue='minha_fila',
  routing_key='create.instagram'
)

# Configura a função de callback para receber as mensagens
channel.basic_consume(queue='minha_fila', on_message_callback=callback, auto_ack=True)

# Inicia o consumo de mensagens
channel.start_consuming()
