import time

from pageObject.SignInPage import SignInPage
from pageObject.ShoppingPage import ShoppingPage
from pageObject.SignOutPage import SignOutPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_002_Shopping():
    baseUrl = ReadConfig.getApplicationURL()
    email = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_shopping(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.sign = SignInPage(self.driver)
        self.sign.clickOnSignIn()
        self.sign.setEmail(self.email)
        self.sign.setPassword(self.password)
        self.sign.clickSignInButton()
        self.logger.info("*** Successfuly signed in ***")

        self.shop = ShoppingPage(self.driver)
        self.shop.hover_over_element()
        self.shop.clickOnTops()
        self.shop.clickOnCategories()
        self.shop.clickOnHoodiesAndSweatshirts()
        self.shop.clickOnStyle()
        self.shop.clickOnSweatshirts()
        self.shop.clickOnProduct()
        self.driver.implicitly_wait(10)
        self.shop.pickSize()
        self.shop.pickAColor()
        self.shop.clickOnAddToCart()
        self.driver.implicitly_wait(15)
        self.shop.clickOnLogo()

        self.signout = SignOutPage(self.driver)
        self.signout.clickOnArrowDown()
        self.signout.clickOnSignOut()
        time.sleep(10)

        act_title = self.driver.title
        if act_title == "Home Page - Magento eCommerce - website to practice selenium | demo website for automation testing | selenium practice sites | selenium demo sites | best website to practice selenium automation | automation practice sites Magento Commerce - website to practice selenium | demo website for automation testing | selenium practice sites":
            assert True
            self.logger.info("*** Added to cart ***")
            self.driver.close()
        else:
            self.logger.error("*** Not added to cart ***")
            self.driver.close()
            assert False