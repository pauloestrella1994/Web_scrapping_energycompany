from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time

url_login = 'https://www.energycompany.com.br/login'

ff = webdriver.Firefox()
ff.get(url_login)

page_html = ff.page_source

page_energy = bs(page_html, 'html.parser')

username = ff.find_element_by_xpath('/html/body/div/div/div/div/form/div/div[2]/div/div[1]/div[1]/div/input')
username.send_keys('pauloestrella1994@gmail.com')

password = ff.find_element_by_xpath(('/html/body/div/div/div/div/form/div/div[2]/div/div[1]/div[2]/div/input'))
password.send_keys('Paulo1994')

button = ff.find_element_by_xpath('/html/body/div/div/div/div/form/div/div[2]/div/div[3]/div/button')
button.click()

time.sleep(2)
busca_cativo = ff.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div[2]/ul/li[3]/a')
busca_cativo.click()

estado = ff.find_element_by_id('react-select-4-input')
estado.send_keys('Paraná')
estado.send_keys(Keys.ENTER)

search_button = ff.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[11]/div/button[2]')
search_button.click()

time.sleep(20)
enterprises_filter_field = ff.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[12]/div/div/div/div[2]/div/div[1]/div/div[1]/div[7]/div/input')

empresas_filtradas = ['Nome Fantasia', 'Categoria CNAE', 'Divisão CNAE', 'Grupo CNAE', 'Classe CNAE', 'CNAE', 'Submercado',
                      'Região', 'Cidade', 'Bairro', 'Email', 'Consumo Classe (12M)', 'Consumo Classe/Subm. (12M)',
                      'Consumo Classe/Subm. Mês', 'Consumo Classe/Estado (12M)', 'Consumo Classe/Estado Mês',
                      'Break-Even Classe/Distr. Mês', 'Break-Even Classe/Distr. 12M', 'Break-Even Classe/Distr./Subm. Mês',
                      'Break-Even Classe/Distr./Subm. 12M', 'Break-Even Classe/Distr./Est. Mês', 'Break-Even Classe/Distr./Est. 12M',
                      'Cresc. Consumo Classe (mês)', 'Cresc. Consumo Classe/Subm. (mês)', 'Cresc. Consumo Classe/Estado (mês)',
                      'Cresc. Consumo Classe (mês ano ant.)', 'Cresc. Consumo Classe/Subm. (mês ano ant.)',
                      'Cresc. Consumo Classe/Estado (mês ano ant.)']
for i in empresas_filtradas:
    enterprises_filter_field.send_keys(i)
    enterprises_filter_field.send_keys(Keys.ENTER)
    time.sleep(0.5)