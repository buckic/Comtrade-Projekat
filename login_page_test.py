from selenium import webdriver
import time
import constants
import locators
import mocked_data

def TestLogin(username, password):
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get(f"{constants.BASE_URL}{constants.LOGIN_PAGE}")
    driver.maximize_window()

    usernameField = driver.find_element_by_css_selector(locators.login_page_username_css_selector)
    passwordField = driver.find_element_by_css_selector(locators.login_page_password_css_selector)

    logInButton = driver.find_element_by_css_selector(locators.login_page_login_button_css_selector)

    usernameField.send_keys(username)
    passwordField.send_keys(password)

    logInButton.click()

    """
    if(driver.current_url==f"{constants.BASE_URL}{constants.SECURE_PAGE}"):
        print(f"Sucessfull login with {username} and {password}")
    else:
        print(f"Bad login for {username} and {password}")
    time.sleep(3)
    """


    TestLogin(podatak["username"], podatak["password"])

