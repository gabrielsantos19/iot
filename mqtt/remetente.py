""""https://github.com/eclipse/paho.mqtt.python"""

import paho.mqtt.client as mqtt
import time


BROKER_HOST = "192.168.56.1"
BROKER_PORT = 1883
ARQUIVO_TESTE = "../arquivos_teste/arquivo_teste_1.txt"


client = mqtt.Client()
client.connect(BROKER_HOST, BROKER_PORT, 60)

with open(ARQUIVO_TESTE, "r") as f:
    for l in f.readlines():
        l = l.encode("utf-8")
        t = time.time_ns()
        print(f"{t} {l}")
        client.publish("ponte/x", l)

client.loop_forever()
#client.disconnect()