import unittest
from BaseTestCases.BaseTestCase import BaseTestCase
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.MyAccount import MyAccount
from ddt import ddt,data,unpack
from DataReader.LoginDataPage import LoginDataPage

@ddt
class TestCase1(BaseTestCase):

    @data(*LoginDataPage.get_data_from_excel('C:/Users/mmaged/Projects/SoundCloud/DataSource/LoginData.xlsx', 'Data'))
    @unpack
    def test_signIn(self,email,password):

        HomePage.click_on_sign_button_click(self)
        self.driver.implicitly_wait(30)
        LoginPage.email_submit(self,email)
        LoginPage.password_submit(self,password)
        LoginPage.submit(self)
        self.driver.implicitly_wait(30)

        self.assertTrue(MyAccount.check_page(self))

if __name__ == '__main__':
    unittest.main()

