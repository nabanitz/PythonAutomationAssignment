from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, "ap_email")
        self.continue_button = (By.XPATH, "//input[@id='continue']")
        self.password_input = (By.XPATH, "//input[@id='ap_password']")
        self.sign_in_button = (By.ID, "signInSubmit")
        self.error_message = (By.CLASS_NAME, "a-list-item")

    def login(self, email, password):
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.continue_button).click()
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.sign_in_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text