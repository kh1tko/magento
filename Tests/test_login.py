import os
import time
from selenium.webdriver.common.by import By
from Pages.LoginPage import Login
from Pages.HomePage import Home
from Configurations.TestData import TestData


class Test_Login:
    def test_loginPageTitle(self, fixturesSetup):
        self.driver = fixturesSetup
        self.driver.get(TestData.URL)
        Home(self.driver).clickSignIn()
        # Take a screenshot
        current_dir = os.path.dirname(__file__)
        screenshot_dir = os.path.join(current_dir, '..', 'Screenshots')
        os.makedirs(screenshot_dir, exist_ok=True)

        screenshot_path = os.path.join(screenshot_dir, 'test_loginPage.png')
        self.driver.save_screenshot(screenshot_path)

        lp = Login(self.driver)
        pageTitle = lp.get_pageTitle()
        assert 'Customer Login' in pageTitle, 'Not a valid Page'

    def test_successfulLogin(self, fixturesSetup):
        self.driver = fixturesSetup
        self.driver.get(TestData.URL)
        self.driver.find_element(By.LINK_TEXT, 'Sign In').click()
        lp = Login(self.driver)
        lp.loginToApp(username=TestData.USERNAME, password=TestData.PASSWORD)
        time.sleep(2)
        pageTitle = lp.get_pageTitle()
        assert 'Home Page' in pageTitle, 'Login Failed'

    def test_invalid_Login(self, fixturesSetup):
        self.driver = fixturesSetup
        self.driver.get(TestData.URL)
        self.driver.find_element(By.LINK_TEXT, 'Sign In').click()
        lp = Login(self.driver)
        lp.loginToApp(username='Ford', password='12345')
        time.sleep(2)
        pageTitle = lp.get_pageTitle()
        assert 'Customer Login' in pageTitle, 'Login Failed'
