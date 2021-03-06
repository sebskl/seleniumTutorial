from selenium import webdriver

class FindByClassTagName():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome("C:\TestFiles\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)

        elementByClassName = driver.find_element_by_class_name("displayed-class")
        elementByClassName.send_keys("Test")

        if elementByClassName is not None:
            print("Element by ClassName found")

        elementByTagName = driver.find_element_by_tag_name("h1")
        print(elementByTagName.text)

        if elementByTagName is not None:
            print("Element by TagName found")


ch = FindByClassTagName()
ch.test()



