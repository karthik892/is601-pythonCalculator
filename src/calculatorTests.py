import unittest
import os
from calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def test_instantiate_calculator(self):
        calc = Calculator()
        self.assertIsInstance(calc, Calculator)

    def test_addition(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        csvRead = CsvReader()
        test_data = csvRead.loadData(dir_path + '\\csv_test\\Unit Test Addition.csv')
        calc = Calculator()
        for row in test_data:
            res = calc.add(row['Value 1'], row['Value 2'])
            exp = int(row['Result'])
            self.assertEqual(res, exp)

    def test_subtraction(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        csvRead = CsvReader()
        test_data = csvRead.loadData(dir_path + '\\csv_test\\Unit Test Subtraction.csv')
        calc = Calculator()
        for row in test_data:
            res = calc.subtract(row['Value 1'], row['Value 2'])
            exp = int(row['Result'])
            self.assertEqual(res, exp)

    def test_multiplication(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        csvRead = CsvReader()
        test_data = csvRead.loadData(dir_path + '\\csv_test\\Unit Test Multiplication.csv')
        calc = Calculator()
        for row in test_data:
            res = calc.multiply(row['Value 1'], row['Value 2'])
            exp = int(row['Result'])
            self.assertEqual(res, exp)

    def test_division(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        csvRead = CsvReader()
        test_data = csvRead.loadData(dir_path + '\\csv_test\\Unit Test Division.csv')
        calc = Calculator()
        for row in test_data:
            res = calc.divide(row['Value 1'], row['Value 2'])
            exp = float(row['Result'])
            self.assertEqual(round(res, 5), round(exp, 5))

    def test_squaring(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        csvRead = CsvReader()
        test_data = csvRead.loadData(dir_path + '\\csv_test\\Unit Test Square.csv')
        calc = Calculator()
        for row in test_data:
            res = calc.square(row['Value 1'])
            exp = float(row['Result'])
            self.assertEqual(round(res, 5), round(exp, 5))




if __name__ == '__main__':
    unittest.main()
