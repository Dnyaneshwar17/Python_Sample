import unittest
from tests.test_sample import SampleTests

class Test_Suite(unittest.TestCase):

    def test_main_class(self):

        self.suite = unittest.TestSuite()
        tc1 = unittest.TestLoader().loadTestsFromTestCase(SampleTests)

        self.suite.addTests([tc1])
        runner = unittest.TextTestRunner()
        runner.run(self.suite)
