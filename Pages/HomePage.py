from selenium.webdriver.common.by import By

class HomePage():

    signIn_btn = (By.XPATH,".//*[@id='content']/div/div/div[1]/div/div[2]/button[1]")


    def click_on_sign_button_click(self):
        signin_click = self.driver.find_element(*HomePage.signIn_btn).click()

