'''
1. What is strategy pattern
2. List out one use case on the go (multiple algos )
3. Which SOLID principle does this pattern follow
4. Draw the rought structure of this pattern (class diagram wise)
5. Does this pattern need interface
6. 
'''

'''
If you want to modify the behaviour of the class
without changing it use Strategy Pattern (Behavioural Pattern)

(+) We want to comply to this principle
    >> Open Closed Principle
    >>__ Open for extension
    >>__ closed for modification


Make the damn thing you want into an interface, & do the logic below it (child classes)
Program at an interface level that is what is means

'''

'''
Revision:
- Forgot to have ABC for strategies

'''

from abc import ABC, abstractmethod

class FilterStrategy(ABC):
    @abstractmethod
    def removeValue(self, val):
        pass

class RemoveNegativeStrategy(FilterStrategy):
    def removeValue(self, val):
        return val < 0
    
class RemoveOddStrategy(FilterStrategy):
    def removeValue(self, val):
        return bool(abs(val) & 1)

class Array:
    def __init__(self, arr):
        self.arr = arr
    
    def filter(self, strategy):
        res = []

        for val in self.arr:
            if not strategy.removeValue(val):
                res.append(val)
        return res

values = Array([-7, -4, -1, 0, 2, 6, 9])

pos_values = values.filter(RemoveNegativeStrategy())
even_values = values.filter(RemoveOddStrategy())

print(pos_values)
print(even_values)


"""
self example 2:
"""
from abc import ABC, abstractmethod

class MathOper(ABC):
    @abstractmethod
    def math_op(self):
        pass

class Addition(MathOper):
    def math_op(self, a, b):
        return a + b

class Substraction(MathOper):
    def math_op(self, a, b):
        return a - b

class Multplication(MathOper):
    def math_op(self, a, b):
        return a * b

class Square(MathOper):
    def math_op(self, a):
        return a ** 2

class Input:
    def __init__(self, a, b=None):
        self.a, self.b = a, b 
    
    def operate(self, strategy: MathOper):
        if self.b is not None:
            return strategy.math_op(self.a, self.b)
        return strategy.math_op(self.a)

res = [
    Input(10, 10).operate(Addition()),
    Input(10, 10).operate(Substraction()),
    Input(10, 10).operate(Multplication()),
    Input(4).operate(Square())
]

print(res)