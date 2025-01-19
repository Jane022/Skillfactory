
from app.calc import Calculator

class TestClass:

    def setup(self):
        self.calc = Calculator

    def adding(self):
        assert self.calc.adding(self, 3,7 == 10)

    def subtraction(self):
        assert self.calc.subtraction(self, 10, 2) == 8

    def multiply(self):
        assert self.calc.multiply(self, 5, 7) == 35

    def division(self):
        assert self.calc.division(self, 30,3 ) == 10



