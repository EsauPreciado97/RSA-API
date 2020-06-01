from flask import Flask, jsonify, request
from rsa import *

app = Flask(__name__)

@app.route('/keygen', methods=['GET'])
def keyGen():
    e, d, N = generateKeys(32)
    keys = {
        "N": N,
        "Private Key": d,
        "Public Key": e
    }
    return jsonify(keys)

@app.route('/encrypt', methods=['GET'])
def encode():

    e = request.args.get('public', default = 1, type = int)
    N = request.args.get('N', default = 1, type = int)
    msg = request.args.get('msg', default = 1, type = str)

    encrypted_msg = encrypt(e, N, msg)

    response = {
        "Message": encrypted_msg,
        "Status": 'Message has been encoded successfully',
    }
    return response

@app.route('/decrypt', methods=['GET'])
def decode():
    d = request.args.get('private', default = 1, type = int)
    N = request.args.get('N', default = 1, type = int)
    cipher = request.args.get('msg', default = 1, type = str)

    decrypted_msg = decrypt(d, N, cipher)

    response = {
        "Status": 'Message has been decoded successfully',
        "Message": decrypted_msg
    }
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)