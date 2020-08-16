from selenium import webdriver

class EnergyCompany:

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.energycompany.com.br/'
        self.class_login = "jss1"

    def navigate(self):
        self.driver.get(self.url)

    def login(self):
        self.driver.find_element_by_class_name(
            self.class_login).click()

##----------------Instancias-------------##

browser = webdriver.Firefox()
start = EnergyCompany(browser)
start.navigate()
start.login()

