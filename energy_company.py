from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time, csv

class EnergyCompany:

    def __init__(self, driver):
        self.driver = driver
        self.url_login = 'https://www.energycompany.com.br/login'
        self.username_data = str(input("Your email: "))
        self.password_data = str(input("Your password: "))
        self.state_data = str(input("Choose what state do you want to crawl: "))

    def navigate(self):
        self.driver.get(self.url_login)

    def login_data(self):
        username_path = self.driver.find_element_by_xpath('/html/body/div/div/div/div/form/div/div[2]/div/div[1]/div[1]/div/input')
        password_path = self.driver.find_element_by_xpath(('/html/body/div/div/div/div/form/div/div[2]/div/div[1]/div[2]/div/input'))
        button = self.driver.find_element_by_xpath('/html/body/div/div/div/div/form/div/div[2]/div/div[3]/div/button')

        username_path.send_keys(self.username_data)
        password_path.send_keys(self.password_data)
        button.click()
        time.sleep(3)

    def busca_cativo(self):
        busca_cativo_button = self.driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div[2]/ul/li[3]/a')
        busca_cativo_button.click()
        time.sleep(3)

    def define_state(self):
        state = self.driver.find_element_by_id('react-select-4-input')
        state.send_keys(self.state_data)
        state.send_keys(Keys.ENTER)

    def search_button(self):
        search_button = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[11]/div/button[2]')
        search_button.click()
        time.sleep(20)

    def enterprises_filters(self):
        filters = ['Nome Fantasia', 'Categoria CNAE', 'Divisão CNAE', 'Grupo CNAE', 'Classe CNAE', 'CNAE', 'Submercado',
                      'Região', 'Cidade', 'Bairro', 'Email', 'Consumo Classe (12M)', 'Consumo Classe/Subm. (12M)',
                      'Consumo Classe/Subm. Mês', 'Consumo Classe/Estado (12M)', 'Consumo Classe/Estado Mês',
                      'Break-Even Classe/Distr. Mês', 'Break-Even Classe/Distr. 12M', 'Break-Even Classe/Distr./Subm. Mês',
                      'Break-Even Classe/Distr./Subm. 12M', 'Break-Even Classe/Distr./Est. Mês', 'Break-Even Classe/Distr./Est. 12M',
                      'Cresc. Consumo Classe (mês)', 'Cresc. Consumo Classe/Subm. (mês)', 'Cresc. Consumo Classe/Estado (mês)',
                      'Cresc. Consumo Classe (mês ano ant.)', 'Cresc. Consumo Classe/Subm. (mês ano ant.)',
                      'Cresc. Consumo Classe/Estado (mês ano ant.)']
        enterprises_filter_field = self.driver.find_element_by_xpath(
            '/html/body/div/div/div[2]/div/div/div/div[12]/div/div/div/div[2]/div/div[1]/div/div[1]/div[7]/div/input')

        for i in filters:
            enterprises_filter_field.send_keys(i)
            enterprises_filter_field.send_keys(Keys.ENTER)

    def write_csv_file(self):
        page_energy = bs(self.driver.page_source, 'html.parser')
        csv_writer = csv.writer(open('energy_company.csv', 'w'))

        #itereable for write data in csv file
        for tr in page_energy.find_all('tr'):
            data = []

            for th in tr.find_all('th'):
                data.append(th.text)

            if data:
                ','.join(data)
                csv_writer.writerow(data)
                continue

            # run to store data

            for td in tr.find_all('td'):
                data.append(td.text.strip())

            if (data):
                ','.join(data)
                csv_writer.writerow(data)


##----------------Instancias-------------##

#full size screen open
chrome_options = Options()
chrome_options.add_argument("--window-size=1080,1080")

browser = webdriver.Chrome(chrome_options=chrome_options)
start = EnergyCompany(browser)
start.navigate()
start.login_data()
start.busca_cativo()
start.define_state()
start.search_button()
start.enterprises_filters()
start.write_csv_file()


