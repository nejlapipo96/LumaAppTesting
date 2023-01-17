from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ShoppingPage:

    def __init__(self, driver):
        self.driver = driver
        self.element_to_hover = driver.find_element(By.XPATH, "//span[normalize-space()='Women']")

    def hover_over_element(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.element_to_hover).perform()

    def clickOnTops(self):
        self.driver.find_element(By.XPATH, "//a[@id='ui-id-9']//span[contains(text(),'Tops')]").click()

    def clickOnCategories(self):
        self.driver.find_element(By.XPATH, "//div[normalize-space()='Category']").click()

    def clickOnHoodiesAndSweatshirts(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Hoodies & Sweatshirts')]").click()

    def clickOnStyle(self):
        self.driver.find_element(By.XPATH, "//div[normalize-space()='Style']").click()

    def clickOnSweatshirts(self):
        self.driver.find_element(By.XPATH, "//body[1]/div[2]/main[1]/div[3]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/ol[1]/li[2]/a[1]").click()

    def clickOnProduct(self):
        self.driver.find_element(By.XPATH, "//a[@href='https://magento.softwaretestingboard.com/circe-hooded-ice-fleece.html']//span[@class='product-image-container']//span[@class='product-image-wrapper']").click()

    def pickSize(self):
        self.driver.find_element(By.ID, "option-label-size-143-item-168").click()

    def pickAColor(self):
        self.driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-57']").click()

    def clickOnAddToCart(self):
        self.driver.find_element(By.XPATH, "//button[@id='product-addtocart-button']").click()

    def clickOnLogo(self):
        self.driver.find_element(By.XPATH, "//a[@aria-label='store logo']//img").click()