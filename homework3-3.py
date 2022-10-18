import matplotlib.pyplot as plt
import numpy as np
import math


def f(x):
    return math.sin(x)

def f_differential_coefficient(F,x,det):
    return [(F(x+det)-F(x-det))/(det*2)]

def f_graph(range):
    x = list(np.arange(-range, range, 0.01))
    y1 = [f(x_i) for x_i in x]
    plt.title("График функции")
    plt.plot(x, y1)
    plt.show()

def f_differential_coefficient_graph(range,det):
    x = list(np.arange(-range, range, 0.01))
    y2= [f_differential_coefficient(f,det,x_i) for x_i in x]
    plt.title("График производной функции")
    plt.plot(x, y2)
    plt.show()

if __name__ == "__main__":
    #f_graph(20)
    det = 0.0001
    f_differential_coefficient_graph(20,det)
    

