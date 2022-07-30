import requests
import threading
import flask


app = flask.Flask(__name__)


@app.route('/', methods=['POST'])
def root_post():
    print(flask.request.form)
    return 'ok\n'


def receber_mensagens():
    app.run(debug=False)


def enviar_mensagem(payload):
    requests.post('http://192.168.56.1:5000', {'payload':payload})


recebedor = threading.Thread(target=receber_mensagens)
recebedor.start()