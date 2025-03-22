from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

@given('I am on the saucedemo homepage')
def step_open_homepage(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()
    time.sleep(2)

@when('I click on the login button')
def step_click_login(context):
    login_button = context.driver.find_element(By.ID, "login-button")
    login_button.click()
    time.sleep(2)

@when('I enter valid credentials')
def step_enter_valid_credentials(context):
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    # context.driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

@then('I should be redirected to the inventory page')
def step_verify_dashboard(context):
    assert "https://www.saucedemo.com/inventory.html" in context.driver.current_url
    context.driver.quit()

@when('I enter invalid username')
def step_enter_invalid_credentials(context):
    context.driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    # context.driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

@when('I enter invalid password')
def step_enter_invalid_credentials(context):
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("WrongPass123")
    # context.driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

@then('I should see an error message')
def step_verify_error_message(context):
    error_element = context.driver.find_element(By.CLASS_NAME, "error-message-container")
    assert "Epic sadface: Username and password do not match any user in this service" in error_element.text
    context.driver.quit()