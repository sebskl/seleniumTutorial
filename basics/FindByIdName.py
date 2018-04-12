from selenium import webdriver

class FindByIdName():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome("C:\TestFiles\chromedriver.exe")
        driver.get(baseUrl)
        elementById = driver.find_element_by_id("name")

        if elementById is not None:
            print("Element by Id found")

        elementByName = driver.find_element_by_name("show-hide")

        if elementByName is not None:
            print("Element by Name found")

ch = FindByIdName()
ch.test()



