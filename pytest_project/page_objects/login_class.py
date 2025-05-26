from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.user_name = (By.XPATH, "//input[@type='text']")
        self.password = (By.XPATH, "//input[@type='password']")
        self.terms_checkbox = (By.XPATH, "//input[@name='terms']")
        self.login_button = (By.XPATH, "//input[@type='submit']")
        self.shop_link = (By.XPATH, "//a[text()='Shop']")

    def login(self, user_name, password):
        self.driver.find_element(*self.user_name).send_keys(user_name)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.terms_checkbox).click()
        self.driver.find_element(*self.login_button).click()

    def open_shop_page(self):
        # Open shop
        self.wait.until(EC.presence_of_element_located(self.shop_link))
        self.driver.find_element(*self.shop_link).click()