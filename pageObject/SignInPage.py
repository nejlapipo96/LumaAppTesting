from selenium.webdriver.common.by import By

class SignInPage:

    def __init__(self, driver):
        self.driver = driver

    def clickOnSignIn(self):
        self.driver.find_element(By.XPATH, "//div[@class='panel header']//a[contains(text(),'Sign In')]").click()

    def setEmail(self, email):
        self.driver.find_element(By.ID, "email").send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, "pass").send_keys(password)

    def clickSignInButton(self):
        self.driver.find_element(By.ID, "send2").click()