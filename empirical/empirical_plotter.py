from matplotlib import pyplot as plt
from copy import copy
from math import ceil

class EmpiricalPlotter:
	def __init__(self, data, title='untitled'):
		self.title = copy(title)

		n = len(data)
		data.sort()

		self.x = list(range(int(data[0] - 1), ceil(data[-1] + 1)))
		self.y = []
		cur = 0
		for i in self.x:
			while cur < len(data) and data[cur] <= i:
				cur += 1

			self.y.append(cur / n)
		

	def plot(self):
		plt.plot(self.x, self.y)
		plt.title(self.title, fontproperties="SimHei")
		plt.savefig('plot/' + self.title)
		plt.show()