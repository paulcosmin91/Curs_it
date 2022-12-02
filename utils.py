from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Utils:

    def __init__(self):
        self.driver = None

    def open_browser(self, browser_type):
        if browser_type == 'Chrome':
            self.driver = webdriver.Chrome()
        elif browser_type == 'Firefox':
            self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        return self.driver

    def close_browser(self):
        self.driver.quit()

    def open_url(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(2)

    def findElementByName(self, name):
        return self.driver.find_element(By.NAME, name)

    def signup(self, fname, lname, phone, email, password):
        self.findElementByName('first_name').send_keys(fname)
        self.findElementByName('last_name').send_keys(lname)
        self.findElementByName('phone').send_keys(phone)
        self.findElementByName('email').send_keys(email)
        self.findElementByName('password').send_keys(password)

        self.driver.find_element(By.XPATH, "//div/span/div[@class='recaptcha-checkbox-border']").click()
        self.driver.find_element(By.ID, "button")


    def send_credentials(self,email, password):
        self.driver.find_element(By.NAME, 'email').send_keys(email)
        self.driver.find_element(By.NAME, 'password').send_keys(password)

    def press_login_button(self):
        self.driver.find_element(By.XPATH,
        "//div/button[@class='btn btn-default btn-lg btn-block effect ladda-button waves-effect']").click()