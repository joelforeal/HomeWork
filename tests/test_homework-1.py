# -*- coding: utf-8 -*-
# prerequisite: Download browser webdrivers you need , then saved under <python>/
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest


class test_crypto_markets(unittest.TestCase):

    # Background:
    #   Given: User only use Chrome Browser
    #   And : Not login their own Crypto.com account
    def setUp(self):
        # 使用 Chrome 的 WebDriver (Latest: Chrome_99.0.4844.51)
        self.driver = webdriver.Chrome()
        # 使用 Firefox 的 WebDriver  (Note: first "F" UPPERCASE !) (Latest: geckodriver-v0.30.0-win64)
        # self.driver = webdriver.Firefox()
        # 使用 Edge 的 WebDriver (Latest: 96.0.1054.62)
        # self.driver = webdriver.Edge( )

        self.driver.maximize_window()
        self.driver.implicitly_wait(6)
        self.target_url = "https://crypto.com/exchange/markets"
        self.verificationErrors = []
        self.accept_next_alert = True

    # Scenario: User want to navigate to trade page of ZIL/USDT
    #     But Not using "search" function.
    #     Given User open page -> https://crypto.com/exchange/markets,
    #     when User click "USDT" of Favorite bar
    #     Then User should be able to click "Trade" button of "ZIL/USDT" (the same line)
    #     And "ZIL/USDT" trading page is launched
    def test_open_zil_usdt_page(self):
        driver = self.driver
        # Open MainPage
        driver.get("https://crypto.com/exchange/markets")
        # Wait for page loading
        print('Sleeping 4 sec...')
        time.sleep(4)

        try:
            # Page should be rendering completed before validating "USDT" element
            self.assertTrue(self.is_element_present(By.XPATH, "//button[contains(text(),'Markets')]"))
            self.assertTrue(self.is_element_present(By.XPATH, "//button[contains(text(),'Sign Up')]"))

            # Before clicking "ZIL/USDT" "Trade" button, make sure Favorites->"USDT" item is available to click (filter)
            self.assertTrue(
                self.is_element_present(By.XPATH, "//button[@class='e-button e-button--primary e-button--small']")
                )
            self.assertTrue(
                self.is_element_present(By.XPATH, "//div[@class='e-tabs__nav default']//div[contains(text(),'USDT')]")
            )

            screenshotImgPath = r'..\screenshots\Markets_mainPage-1.png'
            driver.get_screenshot_as_file(screenshotImgPath)
            print('Screenshot&Save img--->Markets Main page-1 ')

        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Try to scroll element into view
        target = driver.find_element(by=By.XPATH, value="//div[@class='e-tabs__nav-item'][contains(text(),'All')]")
        target.location_once_scrolled_into_view

        # Find USDT element
        # Note:STILL Can't exactly locate "USDT" <---the only issue so far(mark first to run rest of script)
        # driver.find_element(by=By.XPATH, value="//div[@*]//div[contains(text(),'USDT')]").click()

        print('Sleeping 3 sec... waiting for page loading')
        time.sleep(3)
        # Try to scroll element into view
        target = driver.find_element(by=By.XPATH, value="//span[contains(text(),'ZIL')]")
        target.location_once_scrolled_into_view

        # Take screenshot of bottom page of markets
        screenshotImgPath = r'..\screenshots\Markets_mainPage-2.png'
        driver.get_screenshot_as_file(screenshotImgPath)
        print('Screenshot&Save img--->Markets Main page-2 ')

        driver.find_element(by=By.XPATH, value="//span[contains(text(),'ZIL')]")
        driver.find_element(by=By.XPATH, value="//parent::*//span[contains(.,'ZIL')]/following::*[@class='btn-trade "
                    "e-button e-button--primary e-button--medium'][1]").click()


        #Render to ZIL/USDT trading page
        target = driver.find_element(by=By.XPATH, value="//div[@class ='toggle'][contains(text(), ' ZIL/USDT ')]")
        target.location_once_scrolled_into_view

        print('Sleeping 10 sec... to show all data')
        time.sleep(10)

        self.assertTrue(self.is_element_present(By.XPATH, "//div[@class ='toggle'][contains(text(), ' ZIL/USDT ')]"))

        # Take screenshot of ZIL/USDT trading page
        screenshotImgPath = r'..\screenshots\ZIL_USDT_mainPage.png'
        driver.get_screenshot_as_file(screenshotImgPath)
        print('Screenshot&Save img--->ZIL/USDT Main page ')



    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True


    def tearDown(self):
        self.driver.quit()

