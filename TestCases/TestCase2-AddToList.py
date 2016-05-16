import unittest
from BaseTestCases.BaseTestCase import BaseTestCase
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage

class TestCase2(BaseTestCase):

    def test_signIn(self):
        self.driver.find_element(*HomePage.signIn_btn).click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(*LoginPage.email_txt).clear()
        self.driver.find_element(*LoginPage.email_txt).send_keys("menna_maged@yahoo.com")
        self.driver.find_element(*LoginPage.email_cont_btn).click()
        self.driver.find_element(*LoginPage.pass_txt).clear()
        self.driver.find_element(*LoginPage.pass_txt).send_keys("menna1991")
        self.driver.find_element(*LoginPage.submit_btn).click()

    def addToList(self):


if __name__ == '__main__':
    unittest.main()

