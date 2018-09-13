lass LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = ""
    _login_button = ""
	
	    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")
		
    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")


