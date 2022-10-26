import os
import struct

from flask import Flask, request

app = Flask(__name__)


@app.route('/get_data', methods=['GET'])
def get_data():
    return os.urandom(1024)


@app.route('/post_data', methods=['POST'])
def post_data():
    data = request.get_data()
    print(str(data))
    throughput = 436.1239
    return struct.pack('!d', throughput)


if __name__ == '__main__':
    print('hello')
    app.run(port=5050)
