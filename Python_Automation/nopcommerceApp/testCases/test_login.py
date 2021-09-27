import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("*******************************Test_001_Login**********************************************")
        self.logger.info("*******************************Verifying homepage title************************************")
        self.driver = setup
        self.driver.get(self.baseURL)

        homepagetitle = self.driver.title

        if homepagetitle == 'Your store. Login':
            assert True
            self.driver.quit()
            self.logger.info(
                "*******************************test_homePageTitle is passed************************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.quit()
            self.logger.info(
                "*******************************test_homePageTitle is failed************************************")
            assert False

    def test_login(self, setup):
        self.logger.info("*******************************Verifying login test************************************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)

        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        time.sleep(5)

        actualTitle = self.driver.title

        self.lp.clickLogout()

        if actualTitle == 'Dashboard / nopCommerce administration':
            assert True
            self.driver.quit()
            self.logger.info(
                "*******************************test_login is passed************************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.quit()
            self.logger.info(
                "*******************************test_login is failed************************************")
            assert False
