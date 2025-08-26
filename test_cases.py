import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from Capstone.locators import OrangeHRMLocators
from Capstone.pages import LoginPage, PIMPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(OrangeHRMLocators.url)
    yield driver
    driver.quit()

class TestLogin:
    def test_valid_login(self, setup_driver):
        driver = setup_driver
        login_page = LoginPage(driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
        )
        assert "dashboard" in driver.current_url

    def test_invalid_login(self, setup_driver):
        driver = setup_driver
        login_page = LoginPage(driver)
        login_page.enter_username("Admin")
        login_page.enter_password("InvalidPassword")
        login_page.click_login()

        error_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(OrangeHRMLocators.error_message_locator)
        ).text
        assert "Invalid credentials" in error_message

class TestPIM:
    def test_add_employee(self, setup_driver):
        driver = setup_driver
        login_page = LoginPage(driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        pim_page = PIMPage(driver)
        pim_page.go_to_pim()
        pim_page.add_employee("David", "Selvaraj")

        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(OrangeHRMLocators.pim_success)
        ).text
        assert "David Selvaraj" in success_message
