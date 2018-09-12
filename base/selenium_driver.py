from selenium.webdriver.common.by import By
from traceback import print_stack

class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """

	def getElementList(self, locator, locatorType="id"):
        """
        NEW METHOD
        Get list of elements
        """

