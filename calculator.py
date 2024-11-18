class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        pos_a = a if a > 0 else -a
        pos_b = b if b > 0 else -b
        result = 0
        for _ in range(pos_b):
            result = self.add(result, pos_a)
        if a < 0 and b < 0:
            return result
        elif a < 0 or b < 0:
            return -result
        return result

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError
        if a == 0:
            return 0
        result = 0
        negative = (a < 0) != (b < 0)
        a, b = abs(a), abs(b)
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        return -result if negative else result

    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError
        negative = a < 0
        a, b = abs(a), abs(b)
        while a >= b:
            a = self.subtract(a, b)
        return -a if negative else a


# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))
