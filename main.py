from flask import Flask, make_response

DEBUG_MODE = True
SECRET_KEY = 'lkjshdfaoiuh3599*(*Q#pP@()BPB@)R(&@R#G@RX#GR*O#@R#@(*Y@#X)&)(PH@HDFGWwfow;efi7f3p405;mlih98)@&#$ogfid'

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.debug = DEBUG_MODE


# @app.route('/current', methods=['GET'])
# def current():
#     resp = make_response()
#     resp.headers['Location'] = 'http://localhost:9998/hello'
#     resp.status_code = 302
#     return resp

@app.route('/v2/metamodel/', methods=['POST', 'GET'])
def hello():
    return make_response()


@app.route('/v2/event/', methods=['POST', 'GET'])
def hello1():
    return make_response()


if __name__ == '__main__':
    app.run(host="0.0.0.0",
            port=443,
            ssl_context=('/Users/19312808/Documents/серты/certificates/kafka/karka_server.pem',
                         '/Users/19312808/Documents/серты/certificates/kafka/karka_server.key'
                         )
            )