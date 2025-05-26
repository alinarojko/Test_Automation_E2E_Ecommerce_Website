import json
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pytest_project.page_objects.checkout_confirmation_page_class import CheckoutConfirmation
from pytest_project.page_objects.login_class import LoginPage
from pytest_project.page_objects.shop_page_class import ShopPage


file_path = "../data/e2e_ecommerce_shop.json"
with open(file_path, "r") as file:
    file_data = json.load(file)
    test_list = file_data["data"]


@pytest.mark.parametrize("test_list_item", test_list)
@pytest.mark.smoke
def test_e2e(browser_instance,test_list_item):
    driver = browser_instance
    wait = WebDriverWait(driver, 5)
    url = "https://rahulshettyacademy.com/loginpagePractise"
    driver.get(url)

    # login to the shop
    login_page = LoginPage(driver, wait)
    login_page.login(test_list_item["user_name"], test_list_item["password"])

    # Open shop
    login_page.open_shop_page()
    print(login_page.get_title())

    # Find products on the page, add to the cart
    shop_page = ShopPage(driver)
    shop_page.add_to_cart("Blackberry")
    shop_page.go_to_cart()
    print(shop_page.get_title())

    # Checkout page
    checkout_confirmation = CheckoutConfirmation(driver, wait)
    checkout_confirmation.checkout()
    print(checkout_confirmation.get_title())

    # Enter the destination country
    checkout_confirmation.delivery_address("Ukraine")

    # Assert the confirmation message
    checkout_confirmation.validate_order()


