from rand_string import length
from matplotlib import pyplot as plt
from copy import copy, deepcopy

class Plotter:
	def __init__(self, objs, attr):
		n = len(objs)
		data = sorted([attr(obj) for obj in objs])
		self.x = list(range(0, length + 1))
		self.y = []
		cur = 0
		for i in range(length + 1):
			while cur < len(data) and data[cur] <= i:
				cur += 1

			self.y.append(cur / n)
		

	def plot(self):
		plt.plot(self.x, self.y)
		plt.show()