import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_e2e(browser_instance):
    driver = browser_instance
    wait = WebDriverWait(driver, 5)
    url = "https://rahulshettyacademy.com/loginpagePractise"
    driver.get(url)

    # login to the shop
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys("rahulshettyacademy")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("learning")
    driver.find_element(By.XPATH, "//input[@name='terms']").click()
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    # Open shop
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Shop']")))
    driver.find_element(By.XPATH, "//a[text()='Shop']").click()

    # Find products on the page to add to the cart
    products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    # On every product cart look for the name "Blackberry" , add to the cart
    for product in products:
        product_name = product.find_element(By.XPATH, "./div/h4/a").text
        if product_name == "Blackberry":
            product.find_element(By.XPATH, "./div/button").click()
            print(f"{product_name} is added to the cart")

    # Checkout page
    driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
    driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

    # Enter the destination country
    driver.find_element(By.ID, "country").send_keys("Ukraine")
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Ukraine")))
    driver.find_element(By.LINK_TEXT, "Ukraine").click()
    driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()
    print("Success")

    # Assert the confirmation nessage
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-success alert-dismissible']")))
    message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
    assert "Thank you!" in message
    driver.close()
    print("Test passed")
