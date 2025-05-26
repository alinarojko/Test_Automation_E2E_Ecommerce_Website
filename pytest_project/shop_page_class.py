from selenium.webdriver.common.by import By


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_cart = (By.XPATH, "//div[@class='card h-100']")
        self.product_name = (By.XPATH, "./div/h4/a")
        self.add_button = (By.XPATH, "./div/button")
        self.cart_button = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def add_to_cart(self, user_product_name):
        # Find products on the page to add to the cart
        products = self.driver.find_elements(*self.product_cart)

        # On every product cart look for the name "Blackberry" , add to the cart
        for product in products:
            product_name = product.find_element(*self.product_name).text
            if product_name == user_product_name:
                product.find_element(*self.add_button).click()
                print(f"{product_name} is added to the cart")

    def go_to_cart(self):
        # Checkout page
        self.driver.find_element(*self.cart_button).click()
        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

