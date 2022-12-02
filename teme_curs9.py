from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Login(unittest.TestCase):
    def setUp(self) :
        self.chrome=webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.find_element(By.LINK_TEXT, 'Form Authentication').click()
    def tearDown(self) :
        self.chrome.quit()
#1 Test 1
# Verificati ca noul url e corect
    def test_url(self):
        actual=self.chrome.current_url
        expected='https://the-internet.herokuapp.com/login'
        self.assertEqual(expected,actual, ' Url is incorrect')
#2 Test 2
#Verificati ca page title e corect
    def test_page_title(self):
        actual=self.chrome.title
        expected='The Internet'
        self.assertEqual(expected,actual,'Page title is incorrect')
# Test 3
# Verificati textul de pe elementul xpath=//h2 e corect
    def test_text_element(self):
        actual=self.chrome.find_element(By.XPATH,'//h2[text()="Login Page"]').text
        expected ="Login Page"
        self.assertEqual(expected,actual, 'Text element not match')
#Test 4
#Verificati ca butonul de login este displayed
    def test_define(self):
        actual=self.chrome.find_element(By.CLASS_NAME,'radius').is_displayed()
        expected=True
        self.assertEqual(expected, actual, 'Login not displayed')
#Test 5
#Verificati ca atributul href al linkului ‘Elemental Selenium’ e corect
    def test_atribute(self):
        actual=self.chrome.find_element(By.LINK_TEXT,'Elemental Selenium').get_attribute('href')
        expected="http://elementalselenium.com/"
        self.assertEqual(expected, actual, 'Atribute is incorrect')
#Test 6
# Lasati goale user si pass
# Click login
# Verifica ca eroarea e displayed
    def test_error(self):
        self.chrome.find_element(By.CLASS_NAME,'radius').click()
        actual=self.chrome.find_element(By.XPATH,'//div[@id="flash"]').is_displayed()
        expected=True
        self.assertEqual(expected, actual, 'Error messege not displayed')
#Test 7
#Completeaza cu user si pass invalide
#Click login
#Verifica ca mesajul de pe eroare e corect
#Este si un x pus acolo extra asa ca vom folosi solutia de mai jos
    def test_userpass(self):
        self.chrome.find_element(By.NAME,'username').send_keys('anapopescu@gmail.com')
        self.chrome.find_element(By.NAME,'password').send_keys('123456')
        self.chrome.find_element(By.CLASS_NAME,'radius').click()
        actual=WebDriverWait(self.chrome, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div#flash'))).text
        expected='Your username is invalid!'
        self.assertTrue(expected in actual,'Error message text is incorrect')
#Test 8
#Lasati goale user si pass
#Click login
#Apasa x la eroare
#Verifica ca eroarea a disparut
    def test_deleteerror(self):
        self.chrome.find_element(By.CLASS_NAME, 'radius').click()
        self.chrome.find_element(By.XPATH,'//*[@class="close"]').click()
        actual=bool(self.chrome.find_elements(By.CLASS_NAME, 'flash error'))
        expected=False
        self.assertEqual(expected, actual, 'Error messege is displayed')
#Test 9
#Ia ca o lista toate //label
#Verifica textul ca textul de pe ele sa fie cel asteptat (Username si Password)
#Aici e ok sa avem 2 asserturi
    def test_label(self):
       x=self.chrome.find_elements(By.XPATH,'//label')
       actual=x[0].text
       expected='Username'
       self.assertEqual(expected,actual,'Username not found')
       actual=x[1].text
       expected='Password'
       self.assertEqual(expected, actual, 'Password not found')
#Test 10
#Completeaza cu user si pass valide
#Click login
#Verifica ca noul url CONTINE /secure
#Foloseste un explicit wait pentru elementul cu clasa ’flash succes’
#Verifica ca elementul cu clasa=’flash succes’ este displayed
#Verifica ca mesajul de pe acest element CONTINE textul ‘secure area!’
    def test_validate(self):
        self.chrome.find_element(By.NAME,'username').send_keys('tomsmith')
        self.chrome.find_element(By.NAME, 'password').send_keys('SuperSecretPassword!')
        self.chrome.find_element(By.CLASS_NAME, 'radius').click()
        actual=self.chrome.current_url
        expected='secure'
        self.assertTrue(expected in actual,'secure not in url')
        actual = WebDriverWait(self.chrome, 10).until( EC.visibility_of_element_located((By.XPATH, '//div[@class="flash success"]'))).is_displayed()
        expected=True
        self.assertEqual(expected, actual, 'Element not displayed')
        actual = WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="flash success"]'))).text
        expected='secure area!'
        self.assertTrue(expected in actual, 'secure area not in element')
#11
#Completeaza cu user si pass valide
#Click login
#Click logout
#Verifica ca ai ajuns pe https://the-internet.herokuapp.com/login
    def login_logout(self):
        self.chrome.find_element(By.NAME, 'username').send_keys('tomsmith')
        self.chrome.find_element(By.NAME, 'password').send_keys('SuperSecretPassword!')
        self.chrome.find_element(By.CLASS_NAME, 'radius').click()
        self.chrome.find_element(By.CLASS_NAME, 'button secondary radius').click()
        actual=self.chrome.current_url
        expected=''
        self.assertEqual(expected, actual, 'Url not match')
#Test12 - brute force password hacking
    def test_brute_force(self):
        txt=self.chrome.find_element(By.XPATH,'//h4').text
        x=txt.split()
        i=0
        while i < len (x):
            self.chrome.find_element(By.NAME, 'username').send_keys('tomsmith')
            self.chrome.find_element(By.NAME, 'password').send_keys(x[i])
            self.chrome.find_element(By.CLASS_NAME, 'radius').click()
            actual=self.chrome.current_url
            expected='https://the-internet.herokuapp.com/secure'
            if(actual==expected):
                print('Parola secreta este', x[i])
                break
            else:
                print('Nu am gasit parola')
                i+=1













































