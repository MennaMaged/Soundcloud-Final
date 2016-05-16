from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class LoginPage():


    email_txt = (By.ID,"textfield__input-identifier")
    email_cont_btn = (By.CSS_SELECTOR, ".signinForm__cta.sc-button-cta.sc-button.sc-button-large")
    pass_txt = (By.ID,"textfield__input-password")
    submit_btn = (By.XPATH, ".//*[@class='signinWithPassword']/button")
   # error_message = (By.CSS_SELECTOR,".textfield__validation.g-input-message")

    def email_submit(self,email):
        Login_email = self.driver.find_element(*LoginPage.email_txt).clear()
        Login_email_sendkeys = self.driver.find_element(*LoginPage.email_txt).send_keys(email)

    def submit_btn1(self):
        email_submit_btn = self.driver.find_element(*LoginPage.email_cont_btn).click()

    def password_submit(self,password):
        Login_pass = self.driver.find_element(*LoginPage.pass_txt).clear()
        Login_pass_sendkeys = self.driver.find_element(*LoginPage.pass_txt).send_keys(password)

    def submit_btn2(self):
        Login_submit = self.driver.find_element(*LoginPage.submit_btn).click()

    """""""""
    def error_mssg(self):
        try:
            self.driver.find_element(*LoginPage.error_message).is_displayed()
            return True
        except NoSuchElementException:
            return False
            # Validate the correct credintials
            self.assertTrue(LoginPage.error_mssg(self))
    """""""""

