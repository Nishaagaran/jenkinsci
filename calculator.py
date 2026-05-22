class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return a / b

    def power(self, base, exp):
        return base ** exp

    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Modulo by zero is not allowed")
        return a % b

    def square_root(self, n):
        if n < 0:
            raise ValueError("Cannot take square root of a negative number")
        return n ** 0.5
