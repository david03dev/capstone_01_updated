# locators.py
from selenium.webdriver.common.by import By

class OrangeHRMLocators:
    # Login Page Locators
    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")
    
    #
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    # Dashboard URL
    dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    # PIM Page Locators
    #pim_xpath = "//a[@class='oxd-main-menu-item']/span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text()='PIM']"
    pim_menu = (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text()='PIM']")

    add_employee_button = (By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-item' and text()='Add Employee']") 
    first_name_input = (By.XPATH, "//input[@placeholder='First Name']") 
    last_name_input = (By.XPATH, "//input[@placeholder='Last Name']")   
    save_button = (By.XPATH, "//button[@type='submit']") 

    employee_list_button = (By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-item' and text()='Employee List']")


    # Error message locator
    error_message_locator = (By.XPATH, "//div[@class='oxd-alert-content oxd-alert-content--error']")
    
    # Success message locator
    success_message_locator = (By.XPATH, "//div[@class='message success fadable']")

    #PIM Success message
    pim_success = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 --strong']")
