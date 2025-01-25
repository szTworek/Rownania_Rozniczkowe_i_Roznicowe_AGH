import matplotlib.pyplot as plt

def show(nodes, u, n):
    plt.plot(nodes, u, "o--", color='green', markersize=4, label=f"Rozwiązanie MES dla N={n}")

    plt.legend()
    plt.grid(True, linestyle='--', color='blue', alpha=0.5)

    plt.title("Wykres równania transportu ciepła MES")
    plt.ylabel("u(x)")
    plt.xlabel("x")

    plt.show()
