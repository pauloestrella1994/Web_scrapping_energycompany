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

time.sleep(1)
relatorios = ff.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div[2]/ul/li[2]/a')
relatorios.click()

estado = ff.find_element_by_id('react-select-3-input')
estado.send_keys('Paraná')
estado.send_keys(Keys.ENTER)

search_button = ff.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[9]/div/button[2]')
search_button.click()

time.sleep(2)
enterprises_filter_field = ff.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[10]/div/div/div/div[2]/div/div[1]/div/div[1]/div[4]/div/input')
enterprises_filter_field.send_keys('Agente')
enterprises_filter_field.send_keys(Keys.ENTER)