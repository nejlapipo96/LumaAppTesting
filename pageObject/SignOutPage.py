from selenium.webdriver.common.by import By

class SignOutPage:

    def __init__(self, driver):
        self.driver = driver

    def clickOnArrowDown(self):
        self.driver.find_element(By.XPATH, "//div[@class='panel header']//button[@type='button']").click()

    def clickOnSignOut(self):
        self.driver.find_element(By.XPATH, "//div[@aria-hidden='false']//a[normalize-space()='Sign Out']").click()