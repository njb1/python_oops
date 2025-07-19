class Calculator:
    """ 
    A simple calculator class that performs basic arithmetic operations.
    """
    def __init__(self, num1, num2):
        """Initialize the calculator with two numbers."""
        self.num1 = num1
        self.num2 = num2
    
    def calc_add(self):
        """Return the sum of num1 and num2."""
        self.total = self.num1 + self.num2
        return self.total


    def calc_minus(self):
        """Return the difference of num1 and num2."""
        self.total = self.num1 - self.num2
        return self.total
    

    def calc_mult(self):
        """Return the product of num1 and num2."""
        self.total = self.num1 * self.num2
        return self.total
    

    def calc_div(self):
        """Return the quotient of num1 and num2."""
        if self.num2 == 0:
            raise ValueError("Cannot divide by zero")
        self.total = self.num1 // self.num2
        return self.total


class ExtendedCalculator(Calculator):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)
    
    def calc_mod(self):
        if self.num2 == 0:
            raise ValueError("Cannot divide by zero")
        self.total = self.num1 % self.num2
        return self.total


if __name__ == "__main__":
    my_calc = Calculator(4.3, 2.6)
    total = my_calc.calc_add()
    print(total)