# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import uporedi
app = Flask(__name__)
proceseed_text = ""


@app.route("/")
def index():
    return render_template("welcome.html")

@app.route('/', methods=['POST'])
def index_post():
    text = request.form['text']
    processed_text = text.lower()
    uporedi.tehnomanija = []
    uporedi.gigatron = []
    uporedi.get_tehnomanija(processed_text)
    uporedi.get_gigatron(processed_text)

    gigatron = uporedi.gigatron
    tehnomanija = uporedi.tehnomanija

    return render_template("index.html", tehnomanija=tehnomanija, gigatron=gigatron)
if __name__ == '__main__':
    #app.debug = True
    app.run()