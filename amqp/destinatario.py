"""
Autor: Gabriel Oliveira Santos
Referência: https://www.rabbitmq.com/tutorials/tutorial-one-python.html
"""

import time
import pika


CENARIO = 6

BROKER_HOST = "192.168.56.1"
BROKER_PORT = -1
LOG_FILE = f"../_logs/amqp_destinatario_cenario_{CENARIO}_{time.strftime('%Y-%m-%d-%H-%M-%S')}.csv"


log_file = open(LOG_FILE, "w")
contador = 0


parameters = pika.ConnectionParameters(host=BROKER_HOST)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='destinatario')

def callback(ch, method, properties, body):
    #print(" [x] Received %r" % body)
    global contador
    t = time.time_ns()
    payload = body.decode("utf-8")
    print(f"{contador:04},{t},{payload}", file=log_file)
    contador += 1

channel.basic_consume(queue='destinatario', on_message_callback=callback, auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
try:
    print(f'CENARIO={CENARIO}')
    
    channel.start_consuming()
except KeyboardInterrupt:
    connection.close()
finally:
    log_file.close()