"""
Autor: Gabriel Oliveira Santos
"""

import requests
import time
import flask


CENARIO = 6

PONTE_HOST = "192.168.56.1"
PONTE_PORT = 5000
DESTINATARIO_HOST = "192.168.56.103"
DESTINATARIO_PORT = 5001
DESTINATARIO = f"http://{DESTINATARIO_HOST}:{DESTINATARIO_PORT}"
LOG_FILE = f"../_logs/http_ponte_cenario_{CENARIO}_{time.strftime('%Y-%m-%d-%H-%M-%S')}.csv"


log_file = open(LOG_FILE, "w")
app = flask.Flask(__name__)
contador = 0


@app.route('/', methods=['POST'])
def root_post():
    global contador
    t = time.time_ns()
    payload = flask.request.form['p']
    print(f"{contador:04},{t},{payload}", file=log_file)
    requests.post(DESTINATARIO, {'p':payload})
    contador += 1
    return ('', 204)


try:
    print(f'CENARIO={CENARIO}')
    
    app.run(host='0.0.0.0', port=PONTE_PORT, debug=False)
except KeyboardInterrupt:
    pass
finally:
    log_file.close()