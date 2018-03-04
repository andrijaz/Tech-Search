# -*- coding: utf-8 -*--
import requests
from bs4 import BeautifulSoup


def get_tehnomanija(fraza):

    link = "https://www.tehnomanija.rs/index.php?mod=catalog&op=thm_search&search_type=&submited=1&keywords="
    fraze = fraza
    fraze = fraze.replace(" ","+")
    r = requests.get(link+fraze+"&items_per_page=60")
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

    r = requests.get(linkg+frazeg + "&prikaz=grid-view&limit=128")
    linkg = r.text

    soupg = BeautifulSoup(linkg, 'html.parser')

    for p in soupg.find_all("li", class_="item"):
        ime = p.find("a",class_="product-name" ).text.strip()

        if p.find("h5", class_="old-price")== None:
            cena = p.find("h4", class_="final-price").text.strip() #cena bez maloprodajnog popust ili snizenja
        else:
            cena = p.find("h5", class_="old-price").text.strip()  # cena za maloprodajno
        gigatron.append({"ime": ime, "cena": cena})

def get_winwin(fraza):
    link  = "http://www.winwin.rs/catalogsearch/result/index/?limit=28&mode=grid&q="
    fraze = fraza
    fraze = fraze.replace(" ","+")
    r = requests.get(link+fraze)
    link = r.text

    soup = BeautifulSoup(link, 'html.parser')
    for p in soup.find_all("li", class_="item"):
        ime = p.find("a", itemprop="name").text.strip()
        cena = p.find("span", class_="price").text.strip()
        print(ime, cena)
        winwin.append({"ime":ime, "cena":cena})

tehnomanija=[]
gigatron = []
winwin = []
