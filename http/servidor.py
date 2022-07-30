import flask


app = flask.Flask(__name__)

@app.route('/', methods=['POST'])
def root_post():
    print(flask.request.form)
    return 'ok\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)