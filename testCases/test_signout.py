import time

from pageObject.SignInPage import SignInPage
from pageObject.SignOutPage import SignOutPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_003_SignOut():
    baseUrl = ReadConfig.getApplicationURL()
    email = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_signOut(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.signin = SignInPage(self.driver)
        self.signin.clickOnSignIn()
        self.signin.setEmail(self.email)
        self.signin.setPassword(self.password)
        self.signin.clickSignInButton()
        self.logger.info("*** Successfuly signed in ***")

        self.signout = SignOutPage(self.driver)
        self.signout.clickOnArrowDown()
        self.signout.clickOnSignOut()
        time.sleep(10)

        act_title = self.driver.title
        if act_title == "Home Page - Magento eCommerce - website to practice selenium | demo website for automation testing | selenium practice sites | selenium demo sites | best website to practice selenium automation | automation practice sites Magento Commerce - website to practice selenium | demo website for automation testing | selenium practice sites":
            assert True
            self.logger.info("*** Successfuly signed out ***")
            self.driver.close()
        else:
            self.logger.error("*** Error ***")
            self.driver.close()
            assert False