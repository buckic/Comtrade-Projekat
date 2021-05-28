from selenium import webdriver
import constants
import time
import mocked_data
import locators


def LoginPageTest(email, password):
    driver = webdriver.Chrome("chromedriver.exe")

    driver.get("https://comtradeqa.herokuapp.com")
    driver.maximize_window()

    time.sleep(2)
    prijava = driver.find_element_by_css_selector(locators.prijava_dugme_css_selector)
    prijava.click()


    time.sleep(2)
    email_prijava = driver.find_element_by_css_selector(locators.login_page_email_css_selector)
    email_prijava.send_keys(email)

    time.sleep(2)
    korisnicka_sifra = driver.find_element_by_css_selector(locators.login_page_password_css_selector)
    korisnicka_sifra.send_keys(password)

    time.sleep(2)
    login_dugme = driver.find_element_by_css_selector(locators.login_page_login_button_css_selector)
    login_dugme.click()
    
    time.sleep(1)

    log_out=driver.find_element_by_css_selector(locators.logout_page_logout_button_css_selector)
    log_out.click()


for podatak in mocked_data.TEST_DATA_REGISTRATION:
    LoginPageTest(podatak["email"], podatak["password"])