import unittest
import utils

class Test2(unittest.TestCase):
    driver = utils.Utils()
    def test_valid_credential(self):
        self.driver.open_browser('Chrome')
        self.driver.open_url('https://phptravels.net/login/')
        self.driver.send_credentials("alex@gmail.com", "alabala")
        self.driver.press_login_button()

        self.driver.close_browser()
