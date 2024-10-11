# test_cases.py
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages import LoginPage, PIMPage
from locators import OrangeHRMLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


# Page Object for Login Page
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(OrangeHRMLocators.url)

    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        # Wait for the dashboard to load
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")))
        self.assertIn("dashboard", self.driver.current_url)

    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("Admin")
        login_page.enter_password("InvalidPassword")
        login_page.click_login()

        error_message = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(OrangeHRMLocators.error_message_locator)
        ).text
        self.assertEqual(error_message, "Invalid credentials")

    def tearDown(self):
        self.driver.quit()

class TestPIM(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(OrangeHRMLocators.dashboard_url)

        # Log in first
        login_page = LoginPage(self.driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

    def test_add_employee(self):
        pim_page = PIMPage(self.driver)
        pim_page.go_to_pim()
        pim_page.add_employee("David", "Selvaraj")

        time.sleep(5)
        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrangeHRMLocators.pim_success)
        ).text
        self.assertIn("David Selvaraj", success_message)

if __name__ == "__main__":
    unittest.main()
