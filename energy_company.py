from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests


class EnergyCompany:

    def __init__(self, driver):
        self.driver = driver
        self.url_login = 'https://www.energycompany.com.br/login'

    def navigate(self):
        self.driver.get(self.url_login)

    def login_data(self):
        data = {
            "username": "pauloestrella1994@gmail.com",
            "password": "Paulo1994",
            "grant_type": "password"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0"
        }
        with requests.Session() as s:
            request_login = s.post(self.url_login, data=data, headers=headers)
            print(request_login.content)

##----------------Instancias-------------##

browser = webdriver.Firefox()
start = EnergyCompany(browser)
start.navigate()
start.login_data()

