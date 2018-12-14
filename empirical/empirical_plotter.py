from matplotlib import pyplot as plt

class EmpiricalPlotter:
	def __init__(self, data):
		n = len(data)
		data.sort()

		self.x = list(range(data[0] - 1, data[-1] + 1))
		self.y = []
		cur = 0
		for i in range(data[0] - 1, data[-1] + 1):
			while cur < len(data) and data[cur] <= i:
				cur += 1

			self.y.append(cur / n)
		

	def plot(self):
		plt.plot(self.x, self.y)
		plt.title('233')
		plt.show()