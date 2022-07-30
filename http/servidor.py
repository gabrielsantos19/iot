import requests
import threading
import flask


HOST_AND_PORT = 'http://192.168.56.102:5000'
app = flask.Flask(__name__)


@app.route('/', methods=['POST'])
def root_post():
    print(flask.request.form)
    return 'ok\n'


def receber_mensagens():
    app.run(host='0.0.0.0', port=5000, debug=False)


def enviar_mensagem(payload):
    requests.post(HOST_AND_PORT, {'payload':payload})


recebedor = threading.Thread(target=receber_mensagens)
recebedor.start()