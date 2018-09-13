from base.basepage import BasePage


class SampleDemo(BasePage):
   
    _page_valid = "//a[text()='LOG IN']"
    
   def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def sum_numbers(self, a, b):
        result = a+b
        return result

    def string_valid(self, str1, str2):
        result = str2+str1
        return result
    
    
    def page_valid(self):
        driver = self.driver
        result = self.is_element_present(locator=self._page_valid, locator_type="xpath")
        driver.close()
        return result


   
