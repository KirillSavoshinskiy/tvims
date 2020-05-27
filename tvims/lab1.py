import random
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

a = 0
b = 6
n = 20


def accuracy(numberList):
    res = []
    for k in range(n):
        res.append(float('{:.3f}'.format(numberList[k])))
    return res


def generate_variable_row():
    X = [a + random.random() * (b - a) for i in range(n)]
    Y = []
    for j in range(n):
        Y.append(abs(X[j]))
    Y = accuracy(Y)
    Y.sort()
    print("Вариационный ряд", Y)
    c = Counter(Y)
    table = dict(c)
    values = []
    keys = []
    temp = []
    for k, v in table.items():
        table[k] = v / len(Y)
        temp.append(table[k])
        keys.append(k)
    for i in range(len(temp)):
        values.append(sum(temp[:i + 1]))

    print("Таблица")
    for i in range(len(keys)):
        print(keys[i], ' ', round(values[i], 3))

    return keys, values


def show_empir_teor_func(keys, values):
    x = [0]
    y = [0, 0]
    for k, v in enumerate(keys):
        x.extend([v, v])
        y.append(values[k])
        y.append(values[k])
    y.pop()
    y.append(1)
    x.append(6)
    plt.plot(x, y)
    F = lambda yy: (abs(yy) / 6)
    yy = np.linspace(0, 6)
    plt.plot(yy, F(yy), "orange")
    plt.show()


if __name__ == "__main__":
    key, val = generate_variable_row()
    show_empir_teor_func(key, val)
