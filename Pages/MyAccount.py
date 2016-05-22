from selenium.webdriver.common.by import By
import time

class MyAccount():

    title_lbl = (By.XPATH,".//*[@id='content']/div/div/div[1]/div[1]/div/ul/li[1]/a")
    search_txtbox = (By.XPATH,".//*[@class='header__search']/form/input")
    search_btn = (By.XPATH,".//*[@id='app']/header/div/div[2]/div/form/button")
    add_list = (By.XPATH,".//*[@id='content']/div/div/div[3]/div/div/div/ul/li[2]/div/div/div/div[2]/div[4]/div[1]/div/div/button[3]")

    def check_page(self):
        lbl_account = self.driver.find_element(*MyAccount.title_lbl).is_displayed()
        return lbl_account
    def search(self):
        time.sleep(5)
        searchBox = self.driver.find_element(*MyAccount.search_txtbox)
        searchBox.clear()
        searchBox.send_keys("Hello")
        time.sleep(5)
        self.driver.find_element(*MyAccount.search_btn).click()
        time.sleep(5)
        self.driver.find_element(*MyAccount.add_list).click()
        time.sleep(5)






