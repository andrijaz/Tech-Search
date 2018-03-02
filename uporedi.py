# -*- coding: utf-8 -*--
import re, requests
from bs4 import BeautifulSoup


def get_tehnomanija(fraza):

    link = "https://www.tehnomanija.rs/index.php?mod=catalog&op=thm_search&search_type=&submited=1&keywords="
    fraze = fraza
    fraze = fraze.replace(" ","+")
    r = requests.get(link+fraze)
    link = r.text

    soup = BeautifulSoup(link, 'html.parser')

    for p in soup.find_all("div", class_="product-wrap-grid"):
        ime = p.find("div", class_ = "product-name-grid").text.strip()
        cena = p.find("div", class_="price").text.strip()
        tehnomanija.append({"ime":ime, "cena":cena})



def get_gigatron(fraza):

    linkg = "https://www.gigatron.rs/pretraga?pojam="
    frazeg = fraza
    frazeg = frazeg.replace(" ", "+")

    r = requests.get(linkg+frazeg)
    linkg = r.text

    soupg = BeautifulSoup(linkg, 'html.parser')

    for p in soupg.find_all("li", class_="item"):
        ime = p.find("a",class_="product-name" ).text.strip()

        if p.find("h5", class_="old-price")== None:
            cena = p.find("h4", class_="final-price").text.strip() #cena bez maloprodajnog popust ili snizenja
        else:
            cena = p.find("h5", class_="old-price").text.strip()  # cena za maloprodajno
        gigatron.append({"ime": ime, "cena": cena})
tehnomanija=[]
gigatron = []
