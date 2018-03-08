# -*- coding: utf-8 -*-

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
    izabrane = []
    text = request.form['text']
    proceseed_text = text.lower().strip()


    if request.form.get('tehnomanija'):
       izabrane.append('t')
    if request.form.get('gigatron'):
       izabrane.append('g')
    if request.form.get('winwin'):
       izabrane.append('w')
    if len(proceseed_text) == 0:
        return render_template("welcome.html", poruka='Unesi pojam za pretragu', izabrane=izabrane)

    if len(izabrane) != 2 :
        return render_template("welcome.html", poruka='Izaberi 2 firme', izabrane=izabrane)
    else:
        #poruka = 'Prikazujem sve ' + proceseed_text +' koje sam nasao'

        if proceseed_text not in pretrage:
            pretrage.append(proceseed_text)
        if 'g' not in izabrane: #then tehno + winwin
            uporedi.tehnomanija = []
            uporedi.get_tehnomanija(proceseed_text)
            ime1 = 'Tehnomanija'
            firma1 = uporedi.tehnomanija

            uporedi.winwin = []
            uporedi.get_winwin(proceseed_text)
            ime2 = 'Win Win'
            firma2 = uporedi.winwin
        if 't' not in izabrane: #then winwin + giga
            uporedi.winwin = []
            uporedi.get_winwin(proceseed_text)
            ime1 = 'Win Win'
            firma1 = uporedi.winwin

            uporedi.gigatron = []
            uporedi.get_gigatron(proceseed_text)
            ime2 = "Gigatron"
            firma2 = uporedi.gigatron

        if 'w' not in izabrane: #then giga+tehno
            uporedi.tehnomanija = []
            uporedi.get_tehnomanija(proceseed_text)
            ime1 = 'Tehnomanija'
            firma1 = uporedi.tehnomanija

            uporedi.gigatron = []
            uporedi.get_gigatron(proceseed_text)
            ime2 = "Gigatron"
            firma2 = uporedi.gigatron

        return render_template("index.html",ime1=ime1, ime2=ime2,
                           firma1=firma1, firma2=firma2,
                           pretrage=pretrage,
                           rec = proceseed_text, izabrane=izabrane)

if __name__ == '__main__':
    #app.debug = True
    app.run()