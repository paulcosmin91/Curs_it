import unittest
from unittest import runner

import test1
import test2

class TestSuite(unittest.TestSuite):

    def test_suite(self):
        testcases = unittest.TestSuite()
        testcases.addTest([
            unittest.defaultTestLoader.loadTestsFromTestCase(test1),
            unittest.defaultTestLoader.loadTestsFromTestCase(test2)
        ])

        runner.run(testcases)