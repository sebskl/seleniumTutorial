from selenium import webdriver

class FindByLinkText():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome("C:\TestFiles\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)

        elementByLinkText = driver.find_element_by_link_text("Login")

        if elementByLinkText is not None:
            print("Element by LinkText found")

        elementByPartialLinkText = driver.find_element_by_partial_link_text("Pract")

        if elementByPartialLinkText is not None:
            print("Element by Partial LinkText found")


ch = FindByLinkText()
ch.test()



