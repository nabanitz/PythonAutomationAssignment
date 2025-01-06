from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



class AmazonHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "twotabsearchtextbox")

    def search_product(self, product_name):
        self.driver.find_element(*self.search_box).send_keys(product_name)
        self.driver.find_element(*self.search_box).send_keys(Keys.ENTER)
