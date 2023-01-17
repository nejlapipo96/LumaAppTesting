from pageObject.SignInPage import SignInPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_SignIn():
    baseUrl = ReadConfig.getApplicationURL()
    email = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_signin(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.logger.info("*** Signing In ***")
        self.sign = SignInPage(self.driver)
        self.sign.clickOnSignIn()
        self.sign.setEmail(self.email)
        self.sign.setPassword(self.password)
        self.sign.clickSignInButton()

        act_title = self.driver.title
        if act_title == "Home Page - Magento eCommerce - website to practice selenium | demo website for automation testing | selenium practice sites | selenium demo sites | best website to practice selenium automation | automation practice sites Magento Commerce - website to practice selenium | demo website for automation testing | selenium practice sites":
            assert True
            self.logger.info("*** Successfuly signed in ***")
            self.driver.close()
        else:
            self.logger.error("*** Not signed in ***")
            self.driver.close()
            assert False
