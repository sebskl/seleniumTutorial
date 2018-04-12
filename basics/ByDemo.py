from selenium import webdriver
from selenium.webdriver.common.by import By


class ByDemo():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome("C:\TestFiles\chromedriver.exe")
        driver.get(baseUrl)

        elementById = driver.find_element(By.ID, "name")

        if elementById is not None:
            print("Element by ID found")

        elementByXPath = driver.find_element(By.XPATH, "//input[@id='name']")

        if elementByXPath is not None:
            print("Element by XPath found")


ch = ByDemo()
ch.test()



