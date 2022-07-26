import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_produtos = []

produto_nome = str(input('Nome do produto: '))

url_base = 'https://lista.mercadolivre.com.br/'

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})

for produto in produtos:
    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})

    link = produto.find('a', attrs={'class': 'ui-search-link'})

    real = produto.find('span', attrs={'class': 'price-tag-fraction'})

    centavos = produto.find('span', attrs={'class': 'price-tag-cents'})

    #print('Titulo do produto: ', titulo.text)
    #print('Link do produto: ', link['href'])
    if centavos:
        #print('Preço do produto: R$', real.text + ',' + centavos.text)
        lista_produtos.append([titulo.text, link['href'], real.text + ',' + centavos.text])
    else:
        #print('Preço do produto: R$', real.text)
        lista_produtos.append([titulo.text, link['href'], real.text])
    print('\n\n ')

dataframe = pd.DataFrame(lista_produtos, columns=['Titulo', 'Link', 'Valor'])
dataframe.to_excel('Lista de produtos.xlsx', index=False)
#print(lista_produtos)
#print(produto.prettify())