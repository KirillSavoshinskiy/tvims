import random
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


def accuracy(numberList):
    res = []
    for k in range(len(numberList)):
        res.append(float('{:.3f}'.format(numberList[k])))
    return res


def generate_random_row(a, b, N):
    Y = [a + random.random() * (b - a) for i in range(N)]
    Y = accuracy(Y)
    Y = sorted(Y)
    return Y


def task1():
    a = 6
    b = 0
    N = 200
    m = 10

    def create_histogram(Y):
        v = 20
        n = len(Y)
        A = [Y[0]]
        B = [(Y[m] + Y[m - 1]) / 2]
        V = [n / m] * m
        H = [round(B[0] - A[0], 3)]
        F = [V[0] / (n * H[0])]
        for i in range(1, m):
            A.append(B[i - 1])
            if i != m - 1:
                B.append((Y[(v * (i + 1))] + Y[(v * (i + 1)) - 1]) / 2)
            else:
                B.append(Y[-1])
            H.append(round(B[i] - A[i], 3))
            F.append(V[i] / (n * H[i]))
        print("A[i] B[i] v[i] h[i] f[i]")
        A = accuracy(A)
        B = accuracy(B)
        V = accuracy(V)
        H = accuracy(H)
        F = accuracy(F)
        for i in range(m):
            print(A[i], ' ', B[i], ' ', H[i], ' ', V[i], ' ', F[i])
        return A, B, V, H, F

    def plot_hist(A, B, F):
        F = [0] + F + [0]
        B = [A[0]] + B + [B[-1]]
        plt.step(B, F)
        plt.show()

    A, B, V, H, F = create_histogram(generate_random_row(a, b, N))
    plot_hist(A, B, F)

    f = lambda x: (abs(x) / 6)
    p = []
    xi = []
    for i in range(m):
        p.append(f(B[i]) - f(A[i]))
        xi.append(((V[i] - N * p[i]) ** 2) / (N * p[i]))

    for i in range(len(B)):
        print(i + 1, ' ', round(f(A[i]), 3), ' ', round(f(B[i]), 3), ' ', round(p[i], 3), ' ', round(xi[i], 3), ' ',
              round(xi[i], 3))
    print("Хи - квадрат = ", sum(xi))

    if sum(xi) < 21.07:
        print("Нет оснований отклонять выдвинутую гипотезу")
    else:
        print("Гипотеза отклоняется")


def task2():
    a = 6
    b = 0
    N = 30

    def kolmogorov(Y):
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
        x = [0]
        y = [0, 0]
        for k, v in enumerate(keys):
            x.extend([v, v])
            y.append(values[k])
            y.append(values[k])
        y.pop()
        y.append(1)
        x.append(8)
        plt.plot(x, y)
        F = lambda yy: (abs(yy) / 6)
        yy = np.linspace(0, 6)
        plt.plot(yy, F(yy), "orange")
        plt.show()

        M = 0
        for x in range(len(keys)):
            M = max(abs(F(keys[x]) - values[x]), M)

        M *= np.sqrt(N)
        if M < 1.38:
            print("Нет оснований для отклонения")
        else:
            print("Отказ")

    kolmogorov(generate_random_row(a, b, N))


def task3():
    a = 6
    b = 0
    N = 30

    Y = [a + random.random() * (b - a) for i in range(N)]
    Y = accuracy(Y)
    Y = sorted(Y)
    F = [(abs(x) / 6) for x in Y]

    Fn, D = [], []
    for i in range(N):
        Fn.append((i - 0.5) / 50)
        D.append((Fn[i] - F[i]) ** 2)
    print("i x Fn F D")
    for i in range(N):
        print(i + 1, " ", Y[i], " ", Fn[i], " ", round(F[i], 3), " ", round(D[i], 3))

    if (sum(D) + 1 / (12 * 50)) < 0.461 :
        print("Гипотеза верна")
    else:
        print("Гипотеза неверна")


if __name__ == "__main__":
    print("Задание 1")
    task1()
    print("Задание 2")
    task2()
    print("Задание 3")
    task3()
