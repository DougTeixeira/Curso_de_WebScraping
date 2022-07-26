from operator import ipow
from urllib import response


import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# imprimi o html no formato padrao para melhor visualização
# print(site.prettify())

# vá no site, procure por uma div com atributos de classe com esse nome
noticia = site.find('div', attrs={'class': 'feed-post-body'})

#Titulo
titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
print(titulo.text)

#print(noticia.prettify())
#sub Titulo
subtitulo = noticia.find('div', attrs={'class': 'bstn-fd-relatedtext'})
print(subtitulo.text)