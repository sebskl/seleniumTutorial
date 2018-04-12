from selenium import webdriver

class FindByXPath():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome("C:\TestFiles\chromedriver.exe")
        driver.get(baseUrl)
        elementById = driver.find_element_by_id("name")

        elementByXPath = driver.find_element_by_xpath("//input[@id='name']")

        if elementByXPath is not None:
            print("Element by XPath found")

        elementByCss = driver.find_element_by_css_selector("#name")

        if elementByCss is not None:
            print("Element by CSS found")

ch = FindByXPath()
ch.test()



