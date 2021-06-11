from selenium import webdriver
import time
import constants
import locators
import MockedData
import unittest
import requests



class Test(unittest.TestCase):
    def test_login(self):
        for podatak in MockedData.getTestData("MOCK_DATA.json")["login"]:
            driver = webdriver.Chrome("chromedriver.exe")

            driver.get(constants.BASE_URL)
            driver.maximize_window()

            time.sleep(2)
            prijava = driver.find_element_by_css_selector(locators.prijava_dugme_css_selector)
            prijava.click()


            time.sleep(2)
            email_prijava = driver.find_element_by_css_selector(locators.login_page_email_css_selector)
            email_prijava.send_keys(podatak["email"])

            time.sleep(2)
            korisnicka_sifra = driver.find_element_by_css_selector(locators.login_page_password_css_selector)
            korisnicka_sifra.send_keys(podatak["password"])

            time.sleep(2)
            login_dugme = driver.find_element_by_css_selector(locators.login_page_login_button_css_selector)
            login_dugme.click()
            
            time.sleep(3)

            meme = driver.find_element_by_css_selector(locators.meme_css_selector)
            meme.click() 

            self.assertEqual(driver.current_url, f"{constants.BASE_URL}/")
    
    def test_register(self):
        for podatak in MockedData.getTestData("MOCK_DATA.json")["register"]:

            driver = webdriver.Chrome()
            driver.get(constants.BASE_URL)
            driver.maximize_window()

            prijava=driver.find_element_by_css_selector(locators.prijava_dugme_css_selector)
            prijava.click()

            registracija_link=driver.find_element_by_css_selector(locators.registracija_link_css_selector)
            registracija_link.click()

            korisnicko_ime=driver.find_element_by_css_selector(locators.korisnicko_ime_registracija_css_selector)
            korisnicko_ime.send_keys(podatak["username"])

            email_registracija=driver.find_element_by_css_selector(locators.email_registracija_css_selector)
            email_registracija.send_keys(podatak["email"])

            sifra=driver.find_element_by_css_selector(locators.sifra_registracija_css_selector)
            sifra.send_keys(podatak["password"])

            sifra_potvrda=driver.find_element_by_css_selector(locators.sifra_potvrda_registracija_css_selector)
            sifra_potvrda.send_keys(podatak["passwordConfirm"])

            registracija_dugme=driver.find_element_by_css_selector(locators.registracija_dugme_css_selector)
            registracija_dugme.click()

            self.assertEqual(driver.current_url,f"{constants.BASE_URL}{constants.LOGIN_PAGE}")

    def test_logout(self):
        for podatak in MockedData.getTestData("MOCK_DATA.json")["login"]:
            driver = webdriver.Chrome("chromedriver.exe")

            driver.get(constants.BASE_URL)
            driver.maximize_window()

            time.sleep(2)
            prijava = driver.find_element_by_css_selector(locators.prijava_dugme_css_selector)
            prijava.click()


            time.sleep(2)
            email_prijava = driver.find_element_by_css_selector(locators.login_page_email_css_selector)
            email_prijava.send_keys(podatak["email"])

            time.sleep(2)
            korisnicka_sifra = driver.find_element_by_css_selector(locators.login_page_password_css_selector)
            korisnicka_sifra.send_keys(podatak["password"])

            time.sleep(2)
            login_dugme = driver.find_element_by_css_selector(locators.login_page_login_button_css_selector)
            login_dugme.click()
            
            time.sleep(1)

            log_out=driver.find_element_by_css_selector(locators.logout_page_logout_button_css_selector)
            log_out.click()

            self.assertEqual(driver.current_url,f"{constants.BASE_URL}/")

    def test_is_site_online(self):
        response= requests.get(constants.BASE_URL,timeout=10)
        self.assertEqual(response.status_code,200)

        
        


unittest.main()