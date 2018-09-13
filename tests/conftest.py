import pytest
from base.selenium_driver import SeleniumDriver

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    
    
@pytest.yield_fixture(scope="class")
def one_time_browser_setup():
    get_driver = SeleniumDriver(one_time_browser_setup)
    driver = get_driver.select_browser()
    return driver

@pytest.yield_fixture(scope="session")
def session_level():
    print("session level setUp")

@pytest.yield_fixture(scope="module")
def module_level():
    print("module level setUp")


