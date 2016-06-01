import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\TestCases")
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from TestCases.TestCase1 import TestCase1
from TestCases.TestCase2 import TestCase2
sys.path.append("c:\\users\\mmaged\\appdata\\local\\programs\\python\\python35\\lib\\site-packages")
import xmlrunner

test1 = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
test2 = unittest.TestLoader().loadTestsFromTestCase(TestCase2)

regressionTest = unittest.TestSuite([test1, test2])

runner = xmlrunner.XMLTestRunner(output='test-reports')
runner.run(regressionTest)
