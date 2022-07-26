from selenium import webdriver
from time import sleep

navegador = webdriver.Chrome()
navegador.get('https://www.youtube.com/')
sleep(1)

buscar = navegador.find_element_by_tag_name('input')
buscar.send_keys('Houstonfonication')
buscar.submit()
sleep(0.5)

musica = navegador.find_element_by_id('dismissible')
musica.click()
