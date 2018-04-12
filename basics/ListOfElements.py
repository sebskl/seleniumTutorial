from selenium import webdriver

class ListOfElements():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome("C:\TestFiles\chromedriver.exe")
        driver.get(baseUrl)

        elementListByClassName = driver.find_elements_by_class_name("inputs")

        if elementListByClassName is not None:
            print(f"Size of the list is: {str(len(elementListByClassName))}")


ch = ListOfElements()
ch.test()