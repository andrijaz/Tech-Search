# -*- coding: utf-8 -*-
# https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_sort_table_desc
# filter po ceni i ako i ma previse / premalo proizvoda nesto uraditi
from flask import Flask, render_template, request
import uporedi
app = Flask(__name__)
proceseed_text = ""
pretrage = []

@app.route("/")
def index():
    return render_template("welcome.html")

@app.route('/', methods=['POST'])
def index_post():
    text = request.form['text']
    proceseed_text = text.lower()

    uporedi.tehnomanija = []
    uporedi.gigatron = []
    uporedi.get_tehnomanija(proceseed_text)
    uporedi.get_gigatron(proceseed_text)

    if proceseed_text not in pretrage:
        pretrage.append(proceseed_text)
    #else:
     #   pretrage.pop(

    gigatron = uporedi.gigatron
    tehnomanija = uporedi.tehnomanija

    return render_template("index.html", tehnomanija=tehnomanija, gigatron=gigatron, pretrage=pretrage, rec = proceseed_text)
if __name__ == '__main__':
    #app.debug = True
    app.run()