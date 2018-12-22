# n = 100

from numpy.random import normal

class NormalSet:
	def __init__(self):
		self.x = list(reversed(sorted(normal(0, 1, 100))))

	def get_order(self, order):
		return self.x[order - 1]
		