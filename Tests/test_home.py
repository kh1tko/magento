from Pages.HomePage import Home
from Configurations.TestData import TestData


class Test_Home:

    def test_navigationToMenCategory(self, fixturesSetup):
        self.driver = fixturesSetup
        self.driver.get(TestData.URL)
        hp = Home(self.driver)
        hp.clickMenCategoryItem()
        pageTitle = hp.get_pageTitle()
        assert 'Men' in pageTitle, 'Not a valid Page'


