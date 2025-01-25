import numpy as np

def k(x):
    return 1 if x <= 1 else 2 * x


# Obliczanie lokalnej macierzy i wektora dla elementu
def local_matrices(x_i, x_ip1, h):
    gauss_points = np.array([-1, 1]) / np.sqrt(3)  # Punkty Gaussa
    mid = (x_i + x_ip1) / 2  # Środek elementu
    dedx = np.array([-1, 1]) / h  # Gradient funkcji kształtu
    B_loc = np.zeros((2, 2))
    L_loc = np.zeros(2)

    for xi in gauss_points:
        x = mid + h * xi / 2  # Transformacja punktu Gaussa
        e = np.array([1 - xi, 1 + xi]) / 2  # Funkcje kształtu

        for i in range(2):
            L_loc[i] += 100 * x ** 2 * e[i] * h / 2
            for j in range(2):
                B_loc[i, j] += k(x) * dedx[i] * dedx[j] * h / 2

    return B_loc, L_loc


def matrices(N):
    B = np.zeros((N + 1, N + 1))
    L = np.zeros(N + 1)
    grid_points = np.linspace(0, 2, N + 1)  # Węzły siatki

    for element in range(N):
        x_i, x_ip1 = grid_points[element], grid_points[element + 1]
        h = x_ip1 - x_i
        B_loc, L_loc = local_matrices(x_i, x_ip1, h)

        for i in range(2):
            L[element + i] += L_loc[i]
            for j in range(2):
                B[element + i, element + j] += B_loc[i, j]

    # Warunki brzegowe
    B[0, 0] += 1
    L[0] -= 20
    B[-1, :] = 0
    B[-1, -1] = 1
    L[-1] = -20

    return B, L, grid_points
