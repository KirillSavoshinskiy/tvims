import random

import numpy as np
import matplotlib.pyplot as plt


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
    N = 400

    def create_hist_interval(Y):
        M = np.sqrt(N)
        h = [(Y[-1] - Y[0]) / M]
        A = [round(Y[0] + (0 - 1) * h[0], 3)]
        B = []
        for i in range(1, int(M)):
            h.append(round((Y[-1] - Y[0]) / M, 3))
            A.append(round(Y[0] + (i - 1) * h[i], 3))
            B.append(A[i])
            if i == M - 1:
                B.append(round(B[i - 1] + h[0], 3))
        F = []
        count = 0
        for i in range(int(M)):
            for j in range(len(Y)):
                if A[i] <= Y[j] < B[i]:
                    count += 1
            F.append(round(count / (N * h[i]), 3))
            count = 0
        print("i", " ", "A[i]", " ", "B[i]", " ", "F[i]")
        for i in range(int(M)):
            print(i, " ", A[i], " ", B[i], " ", F[i])
        return A, B, F

    def plot_hist(A, B, F):
        F = [0] + F + [0]
        B = [A[0]] + B + [B[-1]]
        plt.step(B, F, label="Равноинтервальный метод")
        plt.legend()
        plt.show()

    def plot_poligon(A, B, F):
        M = np.sqrt(N)
        X = []
        for i in range(int(M)):
            X.append((A[i] + B[i]) / 2)
        plt.plot(X, F, label="Полигон")
        f = lambda y: np.sign(y) / 6
        y = np.linspace(0, 6)
        plt.plot(y, f(y), "orange", label="Эмпир. функция плотности")
        plt.legend()
        plt.show()

    def plot_grouped_empir(B, Y):
        M = np.sqrt(N)
        temp, freq = [], []
        count = 0
        for i in range(int(M)):
            for j in range(len(Y)):
                if A[i] <= Y[j] < B[i]:
                    count += 1
            freq.append(round(count / N, 3))
            count = 0
        for i in range(len(freq)):
            temp.append(sum(freq[:i + 1]))

        empir_x = [0]
        empir_y = [0, 0]
        for k, v in enumerate(B):
            empir_x.extend([v, v])
            empir_y.append(temp[k])
            empir_y.append(temp[k])
        empir_y.pop()
        empir_y.append(0.9)
        empir_x.append(7)
        plt.plot(empir_x, empir_y, label="Сгруппированная эмпирическая функция")
        plt.xlim(0, 6)
        plt.legend()
        plt.show()


    Y = generate_random_row(a, b, N)
    A, B, F = create_hist_interval(Y)
    plot_hist(A, B, F)
    plot_poligon(A, B, F)
    plot_grouped_empir(B, Y)


def task2():
    a = 6
    b = 0
    N = 400

    def create_hist_ver(Y):
        M = np.sqrt(N)
        m = int(N / M)
        A = [Y[0]]
        B = [round((Y[m] + Y[m + 1]) / 2, 3)]
        H = [round(B[0] - A[0], 3)]
        V = [N / m] * m
        F = [round(V[0] / (N * H[0]), 3)]
        for i in range(1, int(M)):
            A.append(B[i - 1])
            if i != M - 1:
                B.append(round((Y[(m * (i + 1))] + Y[(m * (i + 1)) - 1]) / 2, 3))
            else:
                B.append(Y[-1])
            H.append(round(B[i] - A[i], 3))
            F.append(round(V[i] / (N * H[i]), 3))

        print("A[i] B[i] v[i] h[i] f[i]")
        for i in range(m):
            print(A[i], ' ', B[i], ' ', H[i], ' ', V[i], ' ', F[i])
        return A, B, V, H, F

    def plot_hist(A, B, F):
        B = [A[0]] + B + [B[-1]]
        F = [0] + F + [0]
        plt.step(B, F, label="Равновероятностный метод")
        plt.legend()
        plt.show()

    def plot_poligon(A, B, F):
        M = np.sqrt(N)
        X = []
        for i in range(int(M)):
            X.append((A[i] + B[i]) / 2)
        plt.plot(X, F, label="Полигон")
        f = lambda y: np.sign(y) / 6
        y = np.linspace(0, 6)
        plt.plot(y, f(y), "orange", label="Эмпир. функция плотности")
        plt.legend()
        plt.show()

    def plot_grouped_empir(B, Y):
        M = np.sqrt(N)
        temp, freq = [], []
        count = 0
        for i in range(int(M)):
            for j in range(len(Y)):
                if A[i] <= Y[j] < B[i]:
                    count += 1
            freq.append(round(count / N, 3))
            count = 0
        for i in range(len(freq)):
            temp.append(sum(freq[:i + 1]))

        empir_x = [0]
        empir_y = [0, 0]
        for k, v in enumerate(B):
            empir_x.extend([v, v])
            empir_y.append(temp[k])
            empir_y.append(temp[k])
        empir_y.pop()
        empir_y.append(1)
        empir_x.append(7)
        plt.plot(empir_x, empir_y, label="Сгруппированная эмпирическая функция")
        plt.xlim(0, 6)
        plt.legend()
        plt.show()

    def plot_density_empir():
        f = lambda y: np.sign(y) / 6
        y = np.linspace(0, 6)
        plt.plot(y, f(y), "orange", label="Эмпир. функция плотности")
        plt.legend()
        plt.show()

    Y = generate_random_row(a, b, N)
    A, B, V, H, F = create_hist_ver(Y)
    plot_hist(A, B, F)
    plot_poligon(A, B, F)
    plot_grouped_empir(B, Y)


if __name__ == "__main__":
    #task1()
    task2()