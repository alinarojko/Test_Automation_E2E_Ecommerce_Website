import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pytest_project.checkout_confirmation_page_class import CheckoutConfirmation
from pytest_project.login_class import LoginPage
from pytest_project.shop_page_class import ShopPage


def test_e2e(browser_instance):
    driver = browser_instance
    wait = WebDriverWait(driver, 5)
    url = "https://rahulshettyacademy.com/loginpagePractise"
    driver.get(url)

    # login to the shop
    login_page = LoginPage(driver, wait)
    login_page.login()

    # Open shop
    login_page.open_shop_page()

    # Find products on the page, add to the cart
    shop_page = ShopPage(driver)
    shop_page.add_to_cart("Blackberry")
    shop_page.go_to_cart()

    # Checkout page
    checkout_confirmation = CheckoutConfirmation(driver, wait)
    checkout_confirmation.checkout()

    # Enter the destination country
    checkout_confirmation.delivery_address("Ukraine")

    # Assert the confirmation message
    checkout_confirmation.validate_order()


