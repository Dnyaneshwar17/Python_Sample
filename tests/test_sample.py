import unittest
import pytest
from pages.sample_page import SampleDemo


@pytest.mark.usefixtures("class_level")
class SampleTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.add = SampleDemo("class_level")

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
