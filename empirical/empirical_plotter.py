from matplotlib import pyplot as plt
from copy import copy
from math import ceil
import numpy as np
from .mathlib import *
import re


class EmpiricalPlotter:
    def __init__(self, data, title='untitled'):
        self.title = copy(title)
        

        n = len(data)

        self.e = round(sum(data) / n, 4)
        self.var = round(np.var(data), 4)

        data.sort()

        self.x = sorted(list(set(data)))
        self.y = []
        cur = 0

        for i in self.x:
            while cur < len(data) and data[cur] <= i:
                cur += 1

            self.y.append(cur / n)

    def plot(self):
        plt.grid(True)
        plt.plot(self.x, self.y)

        if self.title == 'X':
            self.title += ' 与自由度为 3 的卡方分布'
            x = np.linspace(0, self.x[-1] + 1, 1000)
            y = [chi_square_distribution(i, 3) for i in x]
            plt.plot(x, y)


        if re.match(r'^X(\d*)', self.title):
            plt.xlabel('E=' + str(self.e) + ' var=' + str(self.var))

        if self.title == '1的个数':
            n = 200
            x = list(range(0, n + 1))
            y = [binomial_distribution(i, n, 0.5) for i in x]
            plt.plot(x, y)
            x = np.linspace(0, 200, 1000)
            y = [normal_distribution(i, 100, sqrt(50)) for i in x]
            plt.plot(x, y)

        plt.title(self.title, fontproperties="SimHei")
        plt.savefig('plot/' + self.title)
        plt.show()
        