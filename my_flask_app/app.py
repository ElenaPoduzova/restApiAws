#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Moe Flask приложение в контейнере Docker.'


@app.route("/product/<product_number>/add", methods=['POST'])
def post_product(product_number):
    return "Product " + product_number + " is added"


@app.route("/product/<product_number>", methods=['GET'])
def get_product(product_number):
    return "Product " + product_number + " data"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')