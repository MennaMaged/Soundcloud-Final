import unittest
from BaseTestCases.BaseTestCase import BaseTestCase
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.MyAccount import MyAccount
from ddt import ddt,data,unpack
from DataReader.LoginDataPage import LoginDataPage

@ddt
# We will call base test case first to run this class
class TestCase1(BaseTestCase):
# @data to collect data from this excel sheet from sheet called 'Data'
    @data(*LoginDataPage.get_data_from_excel('C:/Users/mmaged/Projects/SoundCloud/DataSource/LoginData.xlsx', 'Data'))
    @unpack
# This function will take 2 parameters from the previous mentioned excel sheet with the same columns names
    def test_signIn(self,email,password):
        # To click on sign in button
        HomePage.click_on_sign_button_click(self)
        self.driver.implicitly_wait(30)
        # To enter the email address
        LoginPage.email_submit(self,email)
        # To Submit the email through submit button
        LoginPage.submit_btn1(self)

        if LoginPage.error_mssg(self) == True:
            #self.assertEqual(LoginPage.error_message.text,"Enter a valid email address","Not Equal")
            self.assertEqual("Enter a valid email address",self.driver.find_element_by_css_selector("div.textfield__validation.g-input-message").text)
        else:
        # To enter the password
            LoginPage.password_submit(self,password)
        # Final step to submit the pass and login
            LoginPage.submit_btn2(self)
            self.driver.implicitly_wait(30)
        # Validate login :
            self.assertTrue(MyAccount.check_page(self))

if __name__ == '__main__':
    unittest.main()

