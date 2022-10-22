"""
Autor: Gabriel Oliveira Santos
"""

import time
import flask


CENARIO = 6

DESTINATARIO_HOST = "192.168.56.103"
DESTINATARIO_PORT = 5001
LOG_FILE = f"../_logs/http_destinatario_cenario_{CENARIO}_{time.strftime('%Y-%m-%d-%H-%M-%S')}.csv"


log_file = open(LOG_FILE, "w")
app = flask.Flask(__name__)
contador = 0


@app.route('/', methods=['POST'])
def root_post():
    global contador
    t = time.time_ns()
    payload = flask.request.form['p']
    print(f"{contador:04},{t},{payload}", file=log_file)
    contador += 1
    return ('', 204)


try:
    print(f'CENARIO={CENARIO}')
    
    app.run(host='0.0.0.0', port=DESTINATARIO_PORT, debug=False)
except KeyboardInterrupt:
    pass
finally:
    log_file.close()