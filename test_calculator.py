import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Test cases for add() method
    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(100, 200), 300)
        
        # Additional test cases for add() method
        self.assertEqual(self.calc.add(2, 3), 5)  
        self.assertEqual(self.calc.add(-3, -7), -10)  

    # Test cases for subtract() method
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(7, 7), 0)
        self.assertEqual(self.calc.subtract(100, 50), 50)
        
        # Additional test cases for subtract() method
        self.assertEqual(self.calc.subtract(10, 5), 5)  
        self.assertEqual(self.calc.subtract(-5, -10), 5)  

    # Test cases for multiply() method
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(100, 0), 0)
        
        # Additional test cases for multiply() method
        self.assertEqual(self.calc.multiply(2, 5), 10)  
        self.assertEqual(self.calc.multiply(-3, -4), 12)  

    # Test cases for divide() method
    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 2), 2)  
        self.assertEqual(self.calc.divide(7, 3), 2)  
        self.assertEqual(self.calc.divide(9, 3), 3)  
        self.assertEqual(self.calc.divide(100, 5), 20)  
        
        # Additional test cases for divide() method
        self.assertEqual(self.calc.divide(10, 2), 5)  
        with self.assertRaises(ZeroDivisionError): 
            self.calc.divide(5, 0)

    # Test cases for modulo() method
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)  
        self.assertEqual(self.calc.modulo(7, 3), 1)  
        
        # Additional test cases for modulo() method
        self.assertEqual(self.calc.modulo(10, 3), 1)  
        self.assertEqual(self.calc.modulo(20, 6), 2)  
    
    
    def test_fault_in_divide(self):
        with self.assertRaises(ZeroDivisionError):  
            self.calc.divide(5, 0)

    # Test cases for modulo() method (handling negative numbers)
    def test_fault_in_modulo(self):
        self.assertEqual(self.calc.modulo(-5, 2), 1)  
        self.assertEqual(self.calc.modulo(5, -2), 1)  

    # Test cases for add() and subtract() methods with negative numbers
    def test_fault_in_addition_subtraction(self):
        self.assertEqual(self.calc.add(-5, -10), -15)  
        self.assertEqual(self.calc.subtract(-5, -10), 5)  

if __name__ == '__main__':
    unittest.main()
