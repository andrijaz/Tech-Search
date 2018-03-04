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
    proceseed_text = text.lower().strip()

    uporedi.tehnomanija = []
    uporedi.gigatron = []
    uporedi.get_tehnomanija(proceseed_text)
    uporedi.get_gigatron(proceseed_text)

    if proceseed_text not in pretrage:
        pretrage.append(proceseed_text)
    #if (T in izabrane)
    #   uporedi.tehnomanija = [], uporedi.get_tehnomanija(text), ime1 = t, firma1=t
    #elif (G in izabrane)
    #   uporedi.gigatron = [], uporedi.get_gigatron(text), ime1 = t, firma1=g
    #
    ime1 = "Tehnomanija"
    ime2 = "Gigatron"
    ime3 = "WinWin"
    firma1 = uporedi.tehnomanija
    firma2 = uporedi.gigatron
    return render_template("index.html",ime1=ime1, ime2=ime2, firma1=firma1, firma2=firma2, pretrage=pretrage, rec = proceseed_text)
if __name__ == '__main__':
    #app.debug = True
    app.run()