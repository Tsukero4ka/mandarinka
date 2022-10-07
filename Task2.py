import math


class Rational:

    def __init__(self, *values):
        if values:
            if values[1] and isinstance(values[0], int) and isinstance(values[1], int):
                divisor = math.gcd(values[0], values[1])
                self.numerator = values[0] // divisor
                self.denominator = values[1] // divisor
            else:
                raise ValueError("Only integer values allowed! Second values is not zero.")
        else:
            self.numerator = 1
            self.denominator = 1

    def get(self):
        return f'{self.numerator} / {self.denominator}'

    def getfloat(self):
        return self.numerator/self.denominator

    def add(self, second):
        self.numerator = self.numerator * second.denominator + second.numerator * self.denominator
        self.denominator = self.denominator * second.denominator
        return Rational(self.numerator, self.denominator)

    def sub(self, second):
        self.numerator = self.numerator * second.denominator - second.numerator * self.denominator
        self.denominator = self.denominator * second.denominator
        return Rational(self.numerator, self.denominator)


    def mult(self, second):
        self.numerator = self.numerator * second.numerator
        self.denominator = self.denominator * second.denominator
        return Rational(self.numerator, self.denominator)

    def div(self, second):
        self.numerator = self.numerator * second.denominator
        self.denominator = self.denominator * second.numerator
        return Rational(self.numerator, self.denominator)

obj = Rational(4, 12)
obj2 = Rational(6, 18)
obj = obj.add(obj2)
print(obj.get())
print(obj.getfloat())