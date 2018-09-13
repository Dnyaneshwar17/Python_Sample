import unittest
import pytest
from pages.sample_page import SampleDemo


@pytest.mark.usefixtures("one_time_browser_setup")
class SampleTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, one_time_browser_setup):
        self.add = SampleDemo(one_time_browser_setup)

    @pytest.mark.run(order=1)
    def test_method(self):
        result = self.add.sum_numbers(12, 8)
        assert result == 20


    @pytest.mark.run(order=2)
    def test_method2(self):
        result = self.add.sum_numbers(12, 18)
        assert result > 20

    @pytest.mark.run(order=3)
    def test_method3(self):
        result = self.add.string_valid("Hello","Demo")
        assert result == "DemoHello"
        print("assert result:"+result)
        
    @pytest.mark.run(order=4)
    def test_method4(self):
        result = self.add.page_valid()
        assert result == True
        print("assert result:" + result)
    
