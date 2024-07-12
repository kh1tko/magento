from Pages.LoginPage import Login
from Configurations import readProperty
from Utilities.LoggerInfo import LogInfo


class Test_Login:
    logger = LogInfo.logGen()

    def test_logging(self, fixturesSetup):
        self.logger.info('_____test_loginPageTitle_____')
        self.driver = fixturesSetup
        self.logger.info('________Fixture Setup Successfully_create_dWebdriver_instance_________')
        self.driver.get(readProperty.login_url)
        self.logger.info("________Application URL Successfully_retrieved_and_logged_in________")
        lp = Login(self.driver)
        pageTitle = lp.get_pageTitle()
        self.logger.info("________Login Page title Retrieved_successfully_________")
        assert "Customer Login" in pageTitle, "Not a valid Page"
        self.logger.info("________Assertion Passed________")
