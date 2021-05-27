# -*- coding: utf-8 -*-
"""
    :author: Akash Meshram
    :url: http://akashmeshram.github.io
"""
from __future__ import unicode_literals
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
import youtube_dl

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
    return response

@app.route('/transcribe')
def transcribe():
    main()
    response = '<h1>Transcribe Sucessfully</h1>' # escape name to avoid XSS
    return response

@app.route('/get-transcript')
def getTranscript():
    f = open("output/movie.srt", "r")
    return f.read()

ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]',
    'outtmpl': 'movie.%(ext)s',
}
@app.route('/upload')
def videoupload():
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
      ydl.download(['https://www.youtube.com/watch?v=rb_hmW-WiQg'])
    response = 'file uploaded successfully'
    return response

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

# 404
@app.route('/404')
def not_found():
    abort(404)

app.run()