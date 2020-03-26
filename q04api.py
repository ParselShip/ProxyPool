# -*- coding: UTF-8 -*-
from flask import Flask, jsonify
from q03saveDB import ProxyDB


app = Flask(__name__, template_folder='temp')


@app.route('/')
def index():
    return '<h1 align=center> Welcome to ParseShip\'s Proxy Pool </h1>'


@app.route('/get')
def get_proxy():
    client = ProxyDB()
    proxy = client.getOneProxy()
    return jsonify(proxy=proxy,
                   score='10')


@app.route('/proxyNum')
def get_proxyCount():
    client = ProxyDB()
    count = client.testDBProxy()
    return jsonify(allproxy=count,
                   count=len(count))


if __name__ == '__main__':
    app.run()
