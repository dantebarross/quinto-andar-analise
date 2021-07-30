import re
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json


# URL do anúncio
url = 'https://www.quintoandar.com.br/imovel/893382549?house_tags=newAd&search_rank=%7B%22sortMode%22%3A%22relevance%22%2C%22searchMode%22%3A%22list%22%2C%22resultsOrigin%22%3A%22search%22%2C%22rank%22%3A18%2C%22personalization%22%3Atrue%7D&search_id=%22412e522ef0cd11ebaa480e1395c66dd7%22&from_route=%22search_results%22'

option = Options()
option.headless = True # Se for True, não é possível visualizar com interface gráfica
driver = webdriver.Firefox(executable_path='geckodriver\geckodriver.exe') #options=option?

# Abre a URL
driver.get(url)


rua_bairro = driver.find_element_by_class_name("sc-bdVaJa.hOdqiw").text #sc-bdVaJa hOdqiw
print('a rua e bairro são: ' + str(rua_bairro))

preços = driver.find_elements_by_class_name("sc-1mwqqtp-0.byvuTN")#.text

x = 0
while x < len(preços):
    print('os preços são: ' + preços[x].text)
    x += 1



elementos_do_imovel = driver.find_elements_by_class_name("sc-bdVaJa.kxWnCU")#.text

x = 0
while x < len(elementos_do_imovel):
    print('os elementos são: ' + elementos_do_imovel[x].text)
    x += 1


driver.quit()