import unittest
import utils


class Test1(unittest.TestCase):
    driver = utils.Utils()

    def test_create_user(self):
        self.driver.open_browser('Chrome')
        self.driver.open_url('https://phptravels.net/signup')
        self.driver.signup("tibi", "serban", '0733123235', 'serban.tiberiu@gmail.com', 'ItFactory1')
        self.driver.close_browser()
