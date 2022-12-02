import unittest
from HTMLTestRunner import HTMLTestRunner
from teme_curs9 import Login
from test1 import Test1
from test2 import Test2


def test_suite():
    test_cases = unittest.TestSuite()
    test_cases.addTests([
         unittest.defaultTestLoader.loadTestsFromTestCase(Login),
         unittest.defaultTestLoader.loadTestsFromTestCase(Test1),
         unittest.defaultTestLoader.loadTestsFromTestCase(Test2)
    ])
    return test_cases


if __name__ == '__main__':
    runner = HTMLTestRunner(verbosity=2, output="./reports/", report_title='Test report', report_name='report',
                            open_in_browser=True, combine_reports=True)
    runner.run(test_suite())


