import re
import time
import requests
import pandas as pd
from IPython.display import display
from tabulate import tabulate
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

df = pd.DataFrame(columns = ['Name', 'Age'])
print(tabulate(df,headers = 'keys', tablefmt = 'psql'))