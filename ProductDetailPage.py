from selenium.webdriver.common.by import By


class ProductDetailsPage:
    def __init__(self, driver):
        self.driver = driver
        self.buy_now_button = (By.ID, "buy-now-button")

    def click_buy_now(self):
        self.driver.find_element(*self.buy_now_button).click()