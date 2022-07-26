from os import link
from turtle import pd
import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

lista_noticias = []

# imprimi o html no formato padrao para melhor visualização
# print(site.prettify())

# vá no site, procure por uma div com atributos de classe com esse nome
noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:
    #Titulo
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
    #print(titulo.text)
    #print(titulo['href']) #link da noticia

    #print(noticia.prettify())
    #sub Titulo
    subtitulo = noticia.find('div', attrs={'class': 'bstn-fd-relatedtext'})
    if subtitulo:
        #print(subtitulo.text)
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text, '', titulo['href']])

news = pd.DataFrame(lista_noticias, columns=['titulo', 'subtitulo', 'link'])
news.to_excel('Noticias.xlsx', index=False)

#print(news)