from selenium import webdriver
from bs4 import BeautifulSoup as bs

class EnergyCompany:

    def __init__(self, driver):
        self.driver = driver
        self.url_login = 'https://www.energycompany.com.br/login'

    def navigate(self):
        self.driver.get(self.url_login)

    def login_data(self):
        username_path = self.driver.find_element_by_xpath('/html/body/div/div/div/div/form/div/div[2]/div/div[1]/div[1]/div/input')
        password_path = self.driver.find_element_by_xpath(('/html/body/div/div/div/div/form/div/div[2]/div/div[1]/div[2]/div/input'))
        button = self.driver.find_element_by_xpath('/html/body/div/div/div/div/form/div/div[2]/div/div[3]/div/button')

        username_data = str(input('Email: '))
        password_data = str(input('Password: '))
        username_path.send_keys(username_data)
        password_path.send_keys(password_data)
        button.click()

##----------------Instancias-------------##

browser = webdriver.Firefox()
start = EnergyCompany(browser)
start.navigate()
start.login_data()

