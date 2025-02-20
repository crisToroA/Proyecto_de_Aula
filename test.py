import unittest
import main

class tests(unittest.TestCase):

    def test_normal_1(self):
        uvt_value = 47065
        gross_income = 100_000_000
        costs_deductions = 10_000_000
        exempt_income = 5_000_000
        tax_discounts = 500_000
        withholdings = 1_000_000
        patrimony = 200_000_000
        rate = 0.28
    
        expected_result = 85_000_000, 1_806, 28, 22_300_000, 0

        calculated_tax = main.tax_payment(uvt_value, gross_income, costs_deductions, exempt_income, tax_discounts, withholdings, patrimony)
        
        self.assertEqual(calculated_tax, expected_result)
     def test_normal_2(self):
        uvt_value = 47065
        gross_income = 100_000_000
        costs_deductions = 0
        exempt_income = 0
        tax_discounts = 0
        withholdings = 1_000_000
        patrimony = 200_000_000
        rate = 0.19

        expected_result = 70_000_000, 1_487, 19, 12_300_000, 0

        calculated_tax = main.tax_payment(uvt_value, gross_income, costs_deductions, exempt_income, tax_discounts, withholdings, patrimony)

        self.assertEqual(calculated_tax, expected_result)
        
    def test_extraordinary_1(self):
        uvt_value = 47065
        gross_income = 500_000_000
        costs_deductions = 50_000_000
        exempt_income = 10_000_000
        tax_discounts = 2_000_000
        withholdings = 5_000_000
        patrimony = 1_000_000_000
    
        expected_result = 440_000_000, 9_349, 35, 147_000_000, 0

        calculated_tax = main.tax_payment(uvt_value, gross_income, costs_deductions, exempt_income, tax_discounts, withholdings, patrimony)
        
        self.assertEqual(calculated_tax, expected_result)

    def test_extraordinary_2(self):
        uvt_value = 47065
        gross_income = 120_000_000
        costs_deductions = 50_000_000
        exempt_income = 20_000_000
        tax_discounts = 0
        withholdings = 500_000
        patrimony = 200_000_000
    
        expected_result = 50_000_000, 1_062, 0, -427_000

        calculated_tax = main.tax_payment(uvt_value, gross_income, costs_deductions, exempt_income, tax_discounts, withholdings, patrimony)
        
        self.assertEqual(calculated_tax, expected_result)

if __name__ == '__main__':
    unittest.main(exit=False)
