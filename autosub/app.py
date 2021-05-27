# -*- coding: utf-8 -*-
"""
    :author: Akash Meshram
    :url: http://akashmeshram.github.io
"""
import os
try:
    from urlparse import urlparse, urljoin
except ImportError:
    from urllib.parse import urlparse, urljoin

from jinja2 import escape
from jinja2.utils import generate_lorem_ipsum
from flask import Flask, make_response, request, redirect, url_for, abort, session, jsonify
from flask_ngrok import run_with_ngrok
from main import main

app = Flask(__name__)
run_with_ngrok(app)

# get name value from query string and cookie
@app.route('/')
@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name', 'Human')
    response = '<h1>Hello, %s!</h1>' % escape(name)  # escape name to avoid XSS
    main()
    return response


# 404
@app.route('/404')
def not_found():
    abort(404)

app.run()