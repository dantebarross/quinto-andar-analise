import re
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import csv

# URL que contém os anúncios da cidade de São Paulo
url = 'https://www.quintoandar.com.br/alugar/imovel/sao-paulo-sp-brasil/'

option = Options()
option.headless = True # Se for True, não é possível visualizar com interface gráfica
driver = webdriver.Firefox(executable_path='geckodriver\geckodriver.exe', options=option) #options=option?

# Abre a URL
driver.get(url)

# Faz o scroll down para mostrar todos os resultados.
time.sleep(15)
div_scroll = driver.find_element_by_class_name('sc-5ca2ou-0.TybLn') #.click() # ou   fmjce0-0.gNNpFx
loop = 61
rangers = 500
urls_coletadas = 0

for i in range(60):
    div_scroll.send_keys(Keys.END)
    time.sleep(1)

for main in range(rangers):
    print("loop: " + str(loop) + " de " + str(rangers))
    loop += 1
    for i in range(10):
        div_scroll.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

    for i in range(7):
        div_scroll.send_keys(Keys.PAGE_UP)
        time.sleep(0.5)

    time.sleep(10)

    # Coleta todas as URLs
    elems = driver.find_elements_by_xpath("//a[@href]")
    time.sleep(5)
    lista_urls = {'urls': []}

    for elem in elems:
        link_geral = str(elem.get_attribute("href"))
        if ('imovel/8') in link_geral:
            #print(link_geral)
            lista_urls['urls'].append(link_geral)

    # Estruturando conteúdo em um arquivo csv
    df = pd.DataFrame(lista_urls)
    df.to_csv('C:/Users/PC/Desktop/quinto-andar-analise/lista_urls/' + str(loop) + '_lista_urls_pandas.csv')
    print('elementos na lista de URLs: ' + str(len(lista_urls['urls'])))
    urls_coletadas = urls_coletadas + len(lista_urls['urls'])
    print(urls_coletadas)

driver.quit()





