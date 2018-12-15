from matplotlib import pyplot as plt
from copy import copy
from math import ceil
import numpy as np
from .mathlib import chi_square_distribution

class EmpiricalPlotter:
	def __init__(self, data, title='untitled'):
		self.title = copy(title)

		n = len(data)
		data.sort()

		self.x = list(range(int(data[0]), ceil(data[-1] + 1)))
		self.y = []
		cur = 0
		for i in self.x:
			while cur < len(data) and data[cur] <= i:
				cur += 1

			self.y.append(cur / n)
		

	def plot(self):
		plt.plot(self.x, self.y)
		

		if self.title == 'X':
			self.title += ' 与自由度为 3 的卡方分布'
			x = np.linspace(0, self.x[-1] + 1, 1000)
			y = [chi_square_distribution(i, 3) for i in x]
			plt.plot(x, y)

		plt.title(self.title, fontproperties="SimHei")
		plt.savefig('plot/' + self.title)
		plt.show()