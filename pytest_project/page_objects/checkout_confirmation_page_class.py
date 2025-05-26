from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CheckoutConfirmation:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.checkout_button = (By.XPATH, "//button[@class='btn btn-success']")
        self.country_input = (By.ID, "country")
        self.country_option = (By.LINK_TEXT, "Ukraine")
        self.terms_cond = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.submit_button = (By.XPATH, "//input[@class='btn btn-success btn-lg']")
        self.success_message = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def checkout(self):
        # Checkout page
        self.driver.find_element(*self.checkout_button).click()
        # driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

    def delivery_address(self, delivery_country):
        self.driver.find_element(*self.country_input).send_keys(delivery_country)
        self.wait.until(EC.presence_of_element_located(self.country_option))
        self.driver.find_element(*self.country_option).click()
        self.driver.find_element(*self.terms_cond).click()
        self.driver.find_element(*self.submit_button).click()

    def validate_order(self):
        self.wait.until(EC.visibility_of_element_located(self.success_message))
        message = self.driver.find_element(*self.success_message).text
        assert "Thank you!" in message

