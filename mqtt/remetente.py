""""https://github.com/eclipse/paho.mqtt.python"""

import paho.mqtt.client as mqtt
import time


BROKER_HOST = "192.168.56.1"
BROKER_PORT = 1883
LOG_FILE = "remetente.csv"
ARQUIVO_TESTE = "../arquivos_teste/arquivo_teste_1.txt"

log_file = open(LOG_FILE, "w")
contador = 0

client = mqtt.Client()
client.connect(BROKER_HOST, BROKER_PORT, 60)

with open(ARQUIVO_TESTE, "r") as f:
    for l in f.readlines():
        l = l[:-1] # Remover o \n no final linha
        e = l.encode("utf-8")
        t = time.time_ns()
        client.publish("ponte/x", e)
        print(f"{contador},{t},{l}", file=log_file)
        contador += 1

try:
    client.loop_forever()
    #client.disconnect()
except KeyboardInterrupt:
    log_file.close()