"""https://www.rabbitmq.com/tutorials/tutorial-one-python.html"""

import pika
import threading


BROKER_HOST = '192.168.56.1'


def receber_dados():
    parameters = pika.ConnectionParameters(host=BROKER_HOST)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='servidor')
    
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        if body == "EOF":
            ch.close()
    
    channel.basic_consume(queue='servidor', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages.')
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        connection.close()


recebedor = threading.Thread(target=receber_dados)
recebedor.start()

parameters = pika.ConnectionParameters(host=BROKER_HOST)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='cliente')

def enviar_dados(payload):
    channel.basic_publish(exchange='', routing_key='cliente', body=payload)

def sair():
    connection.close()
    recebedor.join()