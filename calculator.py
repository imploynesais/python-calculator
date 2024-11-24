class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        # Fix: Subtract b from a (not the other way around)
        return a - b

    def multiply(self, a, b):
        result = 0
        positive_b = abs(b)  # Take absolute value to handle negative numbers
        for i in range(positive_b):
            result = self.add(result, a)  # Add a to the result repeatedly
        # If b is negative, return the negative of the result
        return result if b >= 0 else -result

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        return result
    
    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot perform modulo by zero.")
        while a >= b:
            a = self.subtract(a, b)
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))
