"""
Autor: Gabriel Oliveira Santos
Referência: https://github.com/eclipse/paho.mqtt.python
"""

import paho.mqtt.client as mqtt
import time


CENARIO = 6

BROKER_HOST = "192.168.56.1"
BROKER_PORT = 1883
LOG_FILE = f"../_logs/mqtt_ponte_cenario_{CENARIO}_{time.strftime('%Y-%m-%d-%H-%M-%S')}.csv"


log_file = open(LOG_FILE, "w")
contador = 0


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("ponte/#")


def on_disconnect(client, userdata, rc):
    print(f"Disconnected with result code {rc}")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global contador
    t = time.time_ns()
    payload = msg.payload.decode("utf-8")
    print(f"{contador:04},{t},{payload}", file=log_file)
    client.publish("destinatario/x", msg.payload)
    contador += 1


try:
    print(f'CENARIO={CENARIO}')

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.connect(BROKER_HOST, BROKER_PORT, 60)
    client.loop_forever()
except KeyboardInterrupt:
    pass
finally:
    log_file.close()