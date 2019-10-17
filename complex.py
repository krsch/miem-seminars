"""Реализует класс для работы с комплексными числами

Классы:
    Complex класс комплексных чисел
"""

from dataclasses import dataclass
import math

class Complex:
    """Комплексные числа"""
    re : float = 0
    im : float = 0

    def __init__(self, re :float = 0, im : float = 0):
        self.re = re
        """real part"""
        self.im = im

    def __add__(self, other):
        """суммирует два комплексных числа
        
        Return
            Complex : the sum of two number
        """
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        """вычитает два комплексных числа"""
        return Complex(self.re - other.re, self.im - other.im)

    def __repr__(self):
        return f"Complex(re={self.re}, im={self.im})"

    def __str__(self):
        return f"{self.re} + {self.im}i"

    def __eq__(self, other):
        return self.re == other.re and self.im == other.im

    def __abs__(self):
        return math.sqrt(self.re * self.re + self.im * self.im)