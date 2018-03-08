# -*- coding: utf-8 -*--
import requests
from bs4 import BeautifulSoup


def get_tehnomanija(fraza):

    link = "https://www.tehnomanija.rs/index.php?mod=catalog&op=thm_search&search_type=&submited=1&keywords="

    fraza = fraza.replace(" ","+")
    r = requests.get(link+fraza+"&items_per_page=60")
    link_text = r.text

    soup = BeautifulSoup(link_text, 'html.parser')

    for p in soup.find_all("div", class_="product-wrap-grid"):
        ime = p.find("div", class_ = "product-name-grid").text.strip()
        cena = int(p.find("div", class_="price").text.strip().strip("RSD").replace(".", ""))
        link = p.find("a", class_="product-link").get('href')
        img_link = p.find("img")['src']
        tehnomanija.append({"ime":ime, "cena":cena, "link":link, "slika":img_link})

def get_gigatron(fraza):

    link = "https://www.gigatron.rs/pretraga?pojam="
    fraza = fraza.replace(" ", "+")

    r = requests.get(link+fraza + "&prikaz=grid-view&limit=128")
    link_text = r.text

    soup = BeautifulSoup(link_text, 'html.parser')

    for p in soup.find_all("li", class_="item"):
        ime = p.find("a",class_="product-name" ).text.strip()

        if p.find("h5", class_="old-price")== None:
            cena = p.find("h4", class_="final-price").text.strip() #cena bez maloprodajnog popust ili snizenja
        else:
            cena = p.find("h5", class_="old-price").text.strip()  # cena za maloprodajno
        cena = cena.strip("RSD").strip("MP cena:").replace(".", "")

        link = p.find("a", itemprop="url").get('href')
        img_link = "https://www.gigatron.rs" + p.find("img")['src']

        gigatron.append({"ime": ime, "cena": cena,  "link":link, "slika":img_link})

def get_winwin(fraza):
    link  = "http://www.winwin.rs/catalogsearch/result/index/?limit=28&mode=grid&q="

    fraza = fraza.replace(" ","+")
    r = requests.get(link+fraza)
    link_text = r.text
    soup = BeautifulSoup(link_text, 'html.parser')
    for p in soup.find_all("li", class_="item"):
        ime = p.find("a", itemprop="name").text.strip()
        cena = p.find("span", class_="price").text.strip()
        print(ime, cena)
        winwin.append({"ime":ime, "cena":cena})

tehnomanija=[]
gigatron = []
winwin = []

#print(gigatron)