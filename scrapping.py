import requests
from bs4 import BeautifulSoup

url = 'https://www.energycompany.com.br/dashboard/busca-cativo'
response = requests.get(url)

html = BeautifulSoup(response.text, 'html.parser')

for data in html.select('.jss1'):
    print(data.text)
