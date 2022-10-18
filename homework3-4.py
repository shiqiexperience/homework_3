import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return x**2-y**2

def graph_surface(range):
    ax3 = plt.axes(projection='3d')
    x = np.arange(-range, range, 0.1)
    y = np.arange(-range, range, 0.1)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    ax3.plot_surface(X, Y, Z, cmap='rainbow')
    plt.title("Граф функции")
    plt.show()

def graph_directional_field(range):
    x = np.arange(-range, range, 0.1)
    y = np.arange(-range, range, 0.1)
    X, Y = np.meshgrid(x, y)
    y2 = f(X, Y)
    x2 = np.ones(y2.shape)
    plt.quiver(X, Y, x2, y2, color="red")
    plt.title("Граф поле направлений")
    plt.show()

if __name__ == "__main__":
    graph_surface(3)
    graph_directional_field(1)
