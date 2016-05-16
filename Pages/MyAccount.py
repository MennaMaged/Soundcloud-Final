from selenium.webdriver.common.by import By

class MyAccount():

    title_lbl = (By.XPATH,".//*[@id='content']/div/div/div[1]/div[1]/div/ul/li[1]/a")

    def check_page(self):
        lbl_account = self.driver.find_element(*MyAccount.title_lbl).is_displayed()
        return lbl_account



