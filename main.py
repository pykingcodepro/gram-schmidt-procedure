from vectors import Vector
from typing import List

def gramSchmidtProcess(*vectors:Vector) -> List[Vector]|None:
    n:int = len(vectors)
    vectorList: List[Vector] = list(vectors)
    for v in vectorList:
        if v.getDimension() != n:
            raise TypeError(f"Dimension of every vectors should be equal to number of vectors given: \nvector: {v.getElements()} \ndimenson: {n}")


    orthoBasis:List[Vector] = []
    for v in vectorList:
        if len(orthoBasis) == 0:
            orthoBasis.append(v.normalize())
            continue
        
        tempSum: Vector = Vector(*[ 0 for i in range(n)])
        for e in orthoBasis:
            tempSum += (e.innerProduct(v)*e)
        orthoBasis.append((v-tempSum).normalize())
    return orthoBasis

if __name__ == '__main__':
    v1 = Vector(1, 0, 0)
    v2 = Vector(0, 1, 0)
    v3 = Vector(0, 0, 1)

    basis = gramSchmidtProcess(v1, v2, v3)

    for v in basis:
        v.showVector()