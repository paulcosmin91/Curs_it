from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
# deschidem chrome in modulul controlat de testare automata
chrome = webdriver.Chrome()
chrome.maximize_window()
#navigam catre un URL
chrome.get('https://formy-project.herokuapp.com/autocomplete')
#selector By ID
chrome.find_element(By.ID,'autocomplete').send_keys("Izvorul alb,nr.6")
# selector By Class
chrome.find_elements(By.CLASS_NAME,'form-control')[1].send_keys('Aleea Nucilor nr.3')
#selector By Tag Name
chrome.find_elements(By.TAG_NAME,'input')[2].send_keys("Calea Bucovinei nr.20")
# selector By Path folosind o functie
def formy_input(placeholder_text, input_value):
    input=chrome.find_element(By.XPATH,f'//input[@placeholder="{placeholder_text}"]')
    input.clear()
    input.send_keys(input_value)
formy_input("City","Oradea")
formy_input("State","Bihor")
formy_input("Zip code","725110")
formy_input("Country","Romania")
sleep(3)
#selector By LINK_TEXT
chrome.get('https://formy-project.herokuapp.com')
chrome.find_element(By.LINK_TEXT,'Checkbox').click()
sleep(3)
#Selector By CSS_Selector- ID
chrome.get('https://formy-project.herokuapp.com/checkbox')
chrome.find_element(By.CSS_SELECTOR, "input#checkbox-3").click()
sleep(3)
#Selector By PARTIAL_LINK_TEXT
chrome.get('https://formy-project.herokuapp.com')
chrome.find_element(By.PARTIAL_LINK_TEXT,'Key').click()
sleep(3)
#Selector BY CSS_Selector- Class
chrome.get('https://formy-project.herokuapp.com/keypress')
chrome.find_element(By.CSS_SELECTOR,'input.form-control').send_keys('Popescu Vasile-Aurelian')
#Selector By Xpath atribut-valoare
chrome.find_element(By.XPATH,'//button[@id="button"]').click()
sleep(3)
#Selector By Name
chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
chrome.find_element(By.NAME,'firstname').send_keys('Paul')
# Selector CSS -atribut-valoare partiala
chrome.find_element(By.CSS_SELECTOR,'input[name*="last"]').send_keys("Ionescu")
#Selector Xpath folosind pipe
chrome.find_element(By.XPATH,'//input[@id="sex-0"] | //input[@id="sex"]').click()
#Selector Xpath lista
chrome.find_element(By.XPATH,'(//div/input[@name="exp"])[5]').click()
#Selector Xpath navigare in jos
chrome.find_element(By.XPATH,'//div/div/input[@id="datepicker"]').send_keys('15-11-2022')
#Selector Xpath * toate elementele care respecta regula
chrome.find_element(By.XPATH,'//*[@id="profession-1"]').click()
# Selector Xpath- dupa continut
chrome.find_element(By.XPATH,'//input[contains(@id,"tool-2")]').click()
#Selector Xpath- fratele urmator
chrome.find_element(By.XPATH,'//div/select[@id="continents"]//following-sibling::option[1]').click()
#Selector Xpath- parinte
chrome.find_element(By.XPATH,'//div[@class="controls"]//parent::div/following-sibling::div//select[@id="selenium_commands"]').click()
sleep(3)
#Selector Xpath - dupa text
chrome.get('https://formy-project.herokuapp.com/form')
chrome.find_element(By.XPATH,'//a[text()="Submit"]').click()
sleep(3)
#Selector Xpath- dupa partial text
chrome.get('https://formy-project.herokuapp.com/switch-window')
chrome.find_element(By.XPATH,'//button[contains(text(),"Open ")]').click()
sleep(3)

