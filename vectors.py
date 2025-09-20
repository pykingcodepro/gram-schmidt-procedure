from __future__ import annotations
from typing import List

class Vector:
    def __init__(self, *elements: complex | int) -> None:
        self.elements: List[complex] = [complex(el) for el in elements]
        self.n: int = len(list(elements))
    
    
    def showVector(self) -> None:
        print(self.elements)
    
    def getDimension(self) -> int:
        return self.n
    
    def getElements(self) -> List[complex]:
        return self.elements

    def getNorm(self) -> float:
        sum:complex = 0
        for el in self.elements:
            sum += el.conjugate()*el
        return float((sum.real)**0.5)

    def innerProduct(self, v: Vector) -> float | None:
        if self.n != v.n:
            raise TypeError(f"Both vectors should have same dimension for innerProduct: {self.elements} | {v.elements}")
        
        sum: complex = 0
        for i in range(self.n):
            sum += self.elements[i].conjugate()*v.elements[i]
        return sum
    
    def normalize(self) -> Vector:
        norm = self.getNorm()
        return Vector(*[ el/norm for el in self.elements ])
    
    def __add__(self, v:Vector) -> Vector:
        return Vector(*[ (self.elements[i] + v.elements[i]) for i in range(self.n) ])

    def __sub__(self, v:Vector) -> Vector:
        return Vector(*[ (self.elements[i] - v.elements[i]) for i in range(self.n) ])
    
    def __mul__(self, k:complex|int) -> Vector:
        return Vector(*[ k*el for el in self.elements ])
    
    def __rmul__(self, k:complex|int) -> Vector:
        return Vector(*[ k*el for el in self.elements ])
