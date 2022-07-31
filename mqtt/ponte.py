""""https://github.com/eclipse/paho.mqtt.python"""

import paho.mqtt.client as mqtt


BROKER_HOST = "192.168.56.1"
BROKER_PORT = 1883


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("ponte/#")


def on_disconnect(client, userdata, rc):
    print(f"Disconnected with result code {rc}")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    client.publish("destinatario/x", msg.payload)
    # Encerrar aplicação ao receber mensagem final
    if msg.payload == b'FINALIZAR\n':
        print("FIM")
        client.disconnect()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.connect(BROKER_HOST, BROKER_PORT, 60)
client.loop_forever()