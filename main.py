import os
import struct
import time

from flask import Flask, request

app = Flask(__name__)


@app.route('/get_data', methods=['GET'])
def get_data():
    time.sleep(1)
    return struct.pack('!q 1024s', round(time.time() * 1000), os.urandom(1024))


@app.route('/post_data', methods=['POST'])
def post_data():
    data = request.stream.read()
    return struct.pack('!i', len(data))


if __name__ == '__main__':
    print('hello')
    app.run(port=5050)
