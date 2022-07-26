from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd

options = Options() 
# tamanho da janela que ira abrir
options.add_argument('window-size=400,800')

# faz tudo acontecer sem precisar abrir o navegador
#options.add_argument('--headless')

navegador = webdriver.Chrome(options=options)
navegador.get('https://www.airbnb.com.br/')
sleep(0.5)

#mas caso o conteudo html não venha adequadamente com apenas com o beautifulsoup
#entramos na pagina com o selenium, fazemos sleep e então usamos page_source
#variavel = navegador.page_source #codigo html 
#sleep(2)
# transformador o conteudo em uma melhor leitura com beautifulsoup
#site = BeautifulSoup(navegador.page_source, 'html.parser')
#print(site.prettify()) # imprimir o conteudo html de forma organizada

dados_hospedagens = []

botao_procurar = navegador.find_element_by_class_name('_z8cp555')
botao_procurar.click()
sleep(0.5)

pesquisar = navegador.find_element_by_class_name('_fu0lk47')
pesquisar.send_keys('Ceará')
pesquisar.submit()
sleep(0.5)

botao_local = navegador.find_element_by_css_selector('button > img')
botao_local.click()
sleep(0.5)

data_ida = navegador.find_elements_by_class_name('_12fun97')[32]
data_ida.click()
sleep(0.5)

data_volta = navegador.find_elements_by_class_name('_12fun97')[34]
data_volta.click()
sleep(0.5)

proximo = navegador.find_element_by_class_name('_m3zkvfz')
proximo.click()
sleep(0.5)

adicionar_adulto = navegador.find_elements_by_css_selector('button > span > svg > path[d="m2 16h28m-14-14v28"]')[0]
for i in range(2):
    adicionar_adulto.click()
    sleep(0.5)

sleep(0.5)

adicionar_criança = navegador.find_elements_by_class_name('_8bq7s4')[3]
adicionar_criança.click()
sleep(0.5)

adicionar_animal = navegador.find_elements_by_class_name('_8bq7s4')[7]
adicionar_animal.click()
sleep(0.5)

botao_buscar = navegador.find_element_by_class_name('_14mdb4dc')
botao_buscar.click()
sleep(4)

page_contente = navegador.page_source

site = BeautifulSoup(page_contente, 'html.parser')
#print(site.prettify())

hospedage = site.find('div', attrs={'class': '_1p7qmwaa'})
hospedagens = site.findAll('div', attrs={'class': '_1p7qmwaa'})

for hospedagem in hospedagens:
    local_hospedagem = hospedagem.find('span', attrs={'style': '--title_font-weight:var(--e-y-j-d-v-j); --title_num-lines:1;'})
    print(local_hospedagem.text)
    local_hospedagem = local_hospedagem.text

    detalhes = hospedagem.find('div', attrs={'style': '--margin-bottom:var(--d-b-mrdy);'}).findAll('li')
    #detalhes = detalhes[0].text + detalhes[1].text
    detalhes = ''.join([detalhe.text for detalhe in detalhes])
    print(detalhes)

    estrelas = hospedagem.find('span', attrs={'class': 'rpz7y38 dir dir-ltr'})
    print(estrelas.text)
    estrelas = estrelas.text

    comentario = hospedagem.find('span', attrs={'class': 'rapc1b3 dir dir-ltr'})
    if comentario:
        print(comentario.text)
        comentario = comentario.text

    preço = hospedagem.find('span', attrs={'class': 'a8jt5op dir dir-ltr'})
    print(preço.text)
    preço = preço.text

    preço_total = hospedagem.findAll('span', attrs={'class': 'a8jt5op dir dir-ltr'})[-2]
    print(preço_total.text)
    preço_total = preço_total.text

    hospedagem_link = hospedagem.find('a', attrs={'class': 'l1d1x245 dir dir-ltr'})
    print(hospedagem_link['href'])
    hospedagem_link = 'https://www.airbnb.com.br' + hospedagem_link['href']

    print()
    dados_hospedagens.append([local_hospedagem, detalhes, estrelas, \
        comentario, preço, preço_total, hospedagem_link])

dados = pd.DataFrame(dados_hospedagens,columns=['Local da Hospedagem', 'Detalhes', 'N° de Estrelas',\
     'N° de Comentarios', 'Preço de uma noite', 'Preço Total', 'Link de acesso'])
print(dados)

dados.to_excel('Hospedagens para o Ceará.xlsx')