from concurrent.futures import thread
import pika
import threading


def receber_dados():
    parameters = pika.ConnectionParameters(host='172.17.0.2')
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='hello2')
    #a
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
    #a
    channel.basic_consume(queue='hello2', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


def enviar_dados():
    parameters = pika.ConnectionParameters(host='172.17.0.2')
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='', routing_key='hello', body='Hello World22222!')
    print(" [x] Sent 'Hello World!2222222'")
    connection.close()


t1 = threading.Thread(target=enviar_dados)
t2 = threading.Thread(target=receber_dados)
# t1.start()
t2.start()
# t1.join()
# t2.join()