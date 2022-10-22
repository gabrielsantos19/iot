"""
Autor: Gabriel Oliveira Santos
Referência: https://www.rabbitmq.com/tutorials/tutorial-one-python.html
"""

import time
import pika


CENARIO = 6
INTERVALO = 40    # em milissegundos

BROKER_HOST = "192.168.56.1"
BROKER_PORT = -1    # Não é utilizada
LOG_FILE = f"../_logs/amqp_remetente_cenario_{CENARIO}_{time.strftime('%Y-%m-%d-%H-%M-%S')}.csv"
ARQUIVO_TESTE = f"../_arquivos_teste/cenario_{CENARIO}.txt"
INTERVALO_NS = INTERVALO * 1000000


log_file = open(LOG_FILE, "w")


try:
    print(f'CENARIO={CENARIO}')
    print(f'INTERVALO={INTERVALO}')
    
    parameters = pika.ConnectionParameters(host=BROKER_HOST)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='ponte')

    contador = 0
    t = time.time_ns()
    print(f"INICIO,{t}")
    with open(ARQUIVO_TESTE, "r") as f:
        for l in f.readlines():
            l = l[:-1]    # Remover o \n no final da linha
            t = time.time_ns()
            m = f"{contador:04},{t},{l}"
            e = m.encode("utf-8")
            channel.basic_publish(exchange='', routing_key='ponte', body=m)
            print(contador)
            print(m, file=log_file)
            contador += 1

            delta = INTERVALO_NS - (time.time_ns() - t)
            if delta > 0:
                time.sleep(delta / 1000000000)
    
    # Atraso pré-finalização, para permitir eventuais procedimentos da última mensagem
    time.sleep(5)
    t = time.time_ns()
    print(f"FIM,{t}")
    connection.close()
except KeyboardInterrupt:
    pass
finally:
    log_file.close()