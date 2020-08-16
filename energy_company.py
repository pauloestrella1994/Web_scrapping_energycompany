from selenium import webdriver

class EnergyCompany:

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.energycompany.com.br/'
        self.class_login = "jss1"
        self.class_login_data_email = '/html/body/div/div/div/div/form/div/div[2]/div/div[1]/div[1]/label'
        self.class_login_data_password = '/html/body/div/div/div/div/form/div/div[2]/div/div[1]/div[2]/label'

    def navigate(self):
        self.driver.get(self.url)

    def login(self):
        self.driver.find_element_by_class_name(
            self.class_login).click()

    def login_data(self):
        email = input('Insert your email: ')
        password = input('Insert your password: ')
        self.driver.find_element_by_xpath(self.class_login_data_email).send_keys(email)
        self.driver.find_element_by_xpath(self.class_login_data_password).send_keys(password)


##----------------Instancias-------------##

browser = webdriver.Firefox()
start = EnergyCompany(browser)
start.navigate()
start.login()
start.login_data()

