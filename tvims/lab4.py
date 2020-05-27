import random
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
import scipy.stats as sts


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


def task1(N):
    a = 6
    b = 0
    Y = generate_random_row(a, b, N)
    m = round(sum(Y) / N, 3)
    print("Точечная оценка МО СВ", m)
    D = round(sum([(i - m) ** 2 for i in Y]) / (N - 1), 3)
    print("Точечная оценка дисперсии", D)

    t = sts.t(N - 1)
    arr = t.rvs(1000000)

    def show_disp_and_find_interval(D, m):
        delta1 = sts.mstats.mquantiles(arr, prob=[0.95]) * np.sqrt(D / (N - 1))
        print("Доверительный интервал оценки MO (уровень значимости 0.9):{0}...{1}".format(round(m - delta1[0], 3),
                                                                                           round(m + delta1[0], 3)))
        delta2 = sts.mstats.mquantiles(arr, prob=[0.975]) * np.sqrt(D / (N - 1))
        print("Доверительный интервал оценки MO (уровень значимости 0.95):{0}...{1}".format(round(m - delta2[0], 3),
                                                                                            round(m + delta2[0], 3)))
        delta3 = sts.mstats.mquantiles(arr, prob=[0.99]) * np.sqrt(D / (N - 1))
        print("Доверительный интервал оценки MO (уровень значимости 0.98):{0}...{1}".format(round(m - delta3[0], 3),
                                                                                            round(m + delta3[0], 3)))
        delta4 = sts.mstats.mquantiles(arr, prob=[0.995]) * np.sqrt(D / (N - 1))
        print("Доверительный интервал оценки MO (уровень значимости 0.99):{0}...{1}".format(round(m - delta4[0], 3),
                                                                                            round(m + delta4[0], 3)))
        level = [0.9, 0.95, 0.98, 0.99]
        delts = [2 * delta1[0], 2 * delta2[0], 2 * delta3[0], 2 * delta4[0]]
        plt.plot(level, delts)
        plt.show()
        return level, delts

    level, delts = show_disp_and_find_interval(D, m)

    f = lambda y: ((y - m) ** 2) * np.sign(y) / 6
    D = integrate.quad(f, 0, 6)
    show_disp_and_find_interval(D[0], m)
    return level, delts


def task2(N):
    a = 6
    b = 0
    Y = generate_random_row(a, b, N)
    m = round(sum(Y) / N, 3)
    print("Точечная оценка МО СВ", m)
    D = round(sum([(i - m) ** 2 for i in Y]) / (N - 1), 3)
    print("Точечная оценка дисперсии", D)
    t = sts.chi2(N - 1)
    arr = t.rvs(1000000)

    def show_disp_and_find_interval(D, m):
        D = round(sum([(i - m) ** 2 for i in Y]) / (N - 1), 3)
        delta1 = sts.mstats.mquantiles(arr, prob=[0.25, 0.975])
        print("Доверительный интервал оценки дисперсии(уровень значимости 0.9):{0}...{1}".format(
            round(D - (N - 1) * D / delta1[1], 3),
            round(D + (N - 1) * D / delta1[0], 3)))
        delta2 = sts.mstats.mquantiles(arr, prob=[0.01, 0.99])
        print("Доверительный интервал оценки дисперсии(уровень значимости 0.95):{0}...{1}".format(
            round(D - (N - 1) * D / delta2[1], 3),
            round(D + (N - 1) * D / delta2[0], 3)))
        delta3 = sts.mstats.mquantiles(arr, prob=[0.005, 0.995])
        print("Доверительный интервал оценки дисперсии(уровень значимости 0.98):{0}...{1}".format(
            round(D - (N - 1) * D / delta3[1], 3),
            round(D + (N - 1) * D / delta3[0], 3)))
        level = [0.95, 0.98, 0.99]
        delts = [delta1[1], delta2[1], delta3[1]]
        plt.plot(level, delts)
        plt.show()
        return level, delts

    level, delts = show_disp_and_find_interval(D, m)
    f = lambda y: y * np.sign(y) / 6
    m = integrate.quad(f, 0, 6)
    show_disp_and_find_interval(D, m[0])
    return level, delts


if __name__ == "__main__":
    level1, delts1 = task1(20)
    level2, delts2 = task1(30)
    level3, delts3 = task1(50)
    level4, delts4 = task1(70)
    level5, delts5 = task1(100)
    level6, delts6 = task1(150)
    plt.plot(level1, delts1, label=20)
    plt.plot(level2, delts2, label=30)
    plt.plot(level3, delts3, label=50)
    plt.plot(level4, delts4, label=70)
    plt.plot(level5, delts5, label=100)
    plt.plot(level6, delts6, label=150)
    plt.legend()
    plt.show()

    print("Задание 2")

    level1, delts1 = task1(20)
    level2, delts2 = task1(30)
    level3, delts3 = task1(50)
    level4, delts4 = task1(70)
    level5, delts5 = task1(100)
    level6, delts6 = task1(150)
    plt.plot(level1, delts1, label=20)
    plt.plot(level2, delts2, label=30)
    plt.plot(level3, delts3, label=50)
    plt.plot(level4, delts4, label=70)
    plt.plot(level5, delts5, label=100)
    plt.plot(level6, delts6, label=150)
    plt.legend()
    plt.show()
