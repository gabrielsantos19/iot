""""https://github.com/eclipse/paho.mqtt.python"""

import paho.mqtt.client as mqtt
import time


BROKER_HOST = "192.168.56.1"
BROKER_PORT = 1883
LOG_FILE = "remetente.csv"
ARQUIVO_TESTE = "../arquivos_teste/cenario_4.txt"
INTERVALO = 0.5;

log_file = open(LOG_FILE, "w")


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    

try:
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(BROKER_HOST, BROKER_PORT, 60)
    client.loop_start()

    contador = 0
    t = time.time_ns()
    print(f"INICIO,{t}")
    print(f"INICIO,{t}", file=log_file)
    with open(ARQUIVO_TESTE, "r") as f:
        for l in f.readlines():
            l = l[:-1] # Remover o \n no final da linha
            t = time.time_ns()
            m = f"{contador},{t},{l}"
            e = m.encode("utf-8")
            client.publish("ponte/x", m)
            print(f"{contador},{t}")
            print(m, file=log_file)
            contador += 1
            time.sleep(INTERVALO)
    
    # Atraso pré-finalização, para permitir eventuais procedimentos da última mensagem
    time.sleep(5);
    t = time.time_ns()
    print(f"FIM,{t}")
    print(f"FIM,{t}", file=log_file)
    client.loop_stop(force=False)
except KeyboardInterrupt:
    pass
finally:
    log_file.close()