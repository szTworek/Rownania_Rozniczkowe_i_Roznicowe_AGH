import numpy as np
from solution import matrices
from plot import show

if __name__ == "__main__":
    n = int(input("Liczba elementów: "))
    B, L, nodes = matrices(n)
    u = np.linalg.solve(B, L)

    print(B)
    print(L)

    show(nodes, u , n)