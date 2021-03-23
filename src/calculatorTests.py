import unittest
import os
from calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def test_instantiate_calculator(self):
        calc = Calculator()
        self.assertIsInstance(calc, Calculator)




if __name__ == '__main__':
    unittest.main()
