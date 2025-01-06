from selenium.webdriver.common.by import By

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_titles = (By.CSS_SELECTOR, ".s-title-instructions-style .a-text-normal")

    def get_product_titles(self):
        return self.driver.find_elements(*self.product_titles)

    def click_product_by_index(self, index):
        products = self.get_product_titles()
        if len(products) > index:
            products[index].click()
            return True
        return False