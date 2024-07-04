from Pages.HomePage import Home
from Pages.MenPage import MenPage
from Configurations.TestData import TestData


class Test_EndToEnd:
    def test_addProductToCartAndCheckout(self, fixturesSetup):
        self.driver = fixturesSetup
        self.driver.get(TestData.URL)
        hp = Home(self.driver)
        hp.clickMenCategoryItem()
        mp = MenPage(self.driver)
        mp.addMenPants_first_ToCart_checkout()
        assert hp.get_pageTitle() == 'Checkout'
