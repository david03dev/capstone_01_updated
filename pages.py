# pages.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Capstone.locators import OrangeHRMLocators
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrangeHRMLocators.username_input)
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrangeHRMLocators.password_input)
        ).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrangeHRMLocators.login_button)
        ).click()

class PIMPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_pim(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrangeHRMLocators.pim_menu)
        ).click()

    def add_employee(self, first_name, last_name):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrangeHRMLocators.add_employee_button)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrangeHRMLocators.first_name_input)
        ).send_keys(first_name)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrangeHRMLocators.last_name_input)
        ).send_keys(last_name)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrangeHRMLocators.save_button)
        ).click()
        time.sleep(5)


  
