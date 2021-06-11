from selenium import webdriver
import time
import constants
import locators
import mocked_data

def RegistrationPageTest(username, email, password, passwordConfirm):
    driver = webdriver.Chrome()
    driver.get(constants.BASE_URL)
    driver.maximize_window()

    prijava=driver.find_element_by_css_selector(locators.prijava_dugme_css_selector)
    prijava.click()

    registracija_link=driver.find_element_by_css_selector(locators.registracija_link_css_selector)
    registracija_link.click()

    korisnicko_ime=driver.find_element_by_css_selector(locators.korisnicko_ime_registracija_css_selector)
    korisnicko_ime.send_keys(username)

    email_registracija=driver.find_element_by_css_selector(locators.email_registracija_css_selector)
    email_registracija.send_keys(email)

    sifra=driver.find_element_by_css_selector(locators.sifra_registracija_css_selector)
    sifra.send_keys(password)

    sifra_potvrda=driver.find_element_by_css_selector(locators.sifra_potvrda_registracija_css_selector)
    sifra_potvrda.send_keys(passwordConfirm)

    registracija_dugme=driver.find_element_by_css_selector(locators.registracija_dugme_css_selector)
    registracija_dugme.click()

    print()

    if driver.current_url == f"{constants.BASE_URL}{constants.LOGIN_PAGE}":
        print("Test je uspesno prosao")
    else:
        print("Test je pao")

for podatak in mocked_data.TEST_DATA_REGISTRATION:
    RegistrationPageTest(podatak["username"], podatak["email"], podatak["password"], podatak["passwordConfirm"])