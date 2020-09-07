from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time, csv

url_login = 'https://www.energycompany.com.br/login'

ff = webdriver.Firefox()
ff.get(url_login)

username = ff.find_element_by_xpath('/html/body/div/div/div/div/form/div/div[2]/div/div[1]/div[1]/div/input')
username.send_keys('Testenoenergy@gmail.com')

password = ff.find_element_by_xpath(('/html/body/div/div/div/div/form/div/div[2]/div/div[1]/div[2]/div/input'))
password.send_keys('bizin123')

button = ff.find_element_by_xpath('/html/body/div/div/div/div/form/div/div[2]/div/div[3]/div/button')
button.click()

time.sleep(3)
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

page_html = ff.page_source

page_energy = bs(page_html, 'html.parser')

csv_writer = csv.writer(open('energy_company.csv','w'))

#run loop to extract the table data and store it in csv file
for tr in page_energy.find_all('tr'):
    data = []

    for th in tr.find_all('th'):
        data.append(th.text)

    #run to store metadta in csv file
    if data:
        print('Inserting headers : {}'.format(','.join(data)))
        csv_writer.writerow(data)
        continue

    #run to store data

    for td in tr.find_all('td'):
        data.append(td.text.strip())

    if (data):
        print("Inserting Table Data:{}".format(','.join(data)))
        csv_writer.writerow(data)
