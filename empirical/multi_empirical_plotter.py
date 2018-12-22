from .empirical_plotter import EmpiricalPlotter
from matplotlib import pyplot as plt


class MultiEmpiricalPlotter:
    def __init__(self, title='untitled'):
        self.x, self.y = [], []
        self.title = title[:]

    def add(self, data):
        tmp = EmpiricalPlotter(data)
        self.x.append(tmp.x)
        self.y.append(tmp.y)

    def plot(self):
        plt.grid(True)
        for x, y in zip(self.x, self.y):
            plt.plot(x, y)

        plt.title(self.title, fontproperties="SimHei")
        plt.savefig('plot/' + self.title)

        plt.show()

        