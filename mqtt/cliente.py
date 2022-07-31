""""https://github.com/eclipse/paho.mqtt.python"""

import paho.mqtt.client as mqtt


HOST = "192.168.56.1"
PORT = 1883
ARQUIVO_TESTE = "../arquivos_teste/arquivo_teste_1.txt"


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")
    client.subscribe("cliente/#")
    # Enviar o arquivo teste, uma linha por vez
    with open(ARQUIVO_TESTE, "r") as f:
        for l in f.readlines():
            client.publish("servidor/x", l)


def on_disconnect(client, userdata, rc):
    print(f"Disconnected with result code {rc}")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(str(msg.payload))
    # Encerrar aplicação ao receber mensagem final
    if msg.payload == b'FINALIZAR\n':
        print("FIM")
        client.disconnect()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.connect(HOST, PORT, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()