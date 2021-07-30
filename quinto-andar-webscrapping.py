import re
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

# URL que contém os anúncios da cidade de São Paulo
url = 'https://www.quintoandar.com.br/alugar/imovel/sao-paulo-sp-brasil/'

option = Options()
option.headless = True # Se for True, não é possível visualizar com interface gráfica
driver = webdriver.Firefox(executable_path='geckodriver\geckodriver.exe') #options=option?

# Abre a URL
driver.get(url)

# Faz o scroll down para mostrar todos os resultados.
# Aguardar algum tempo para que todos os resultados sejam mostrados.
# time.sleep(3)
# scrolling_element = driver.find_element_by_xpath("/html/body/div[1]/div/main/section[2]/div[2]/div")
# driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrolling_element)
# time.sleep(300) # Tempo sugerido?

# Coleta todas as URLs
time.sleep(5)
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    link_geral = str(elem.get_attribute("href"))
    if ('imovel/8') in link_geral:
        print(link_geral)


# Parseando conteúdo HTML
# soup = BeautifulSoup(element, 'html.parser')
# anuncio = soup.find('div', attrs={'class': 'sc-1txbuf3-0 dlJilS'})




# Estruturando conteúdo em um Data Frame









driver.quit()
