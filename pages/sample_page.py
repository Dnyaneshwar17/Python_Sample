rom base.basepage import BasePage


class SampleDemo(BasePage):

    # def __init__(self, value):
    #     self.value = value

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def sum_numbers(self, a, b):
        result = a+b
        return result

    def string_valid(self, str1, str2):
        result = str2+str1
        return result

   
