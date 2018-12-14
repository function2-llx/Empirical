from binary_string import BinaryString
from rand_string import rand_string, length
from matplotlib import pyplot as plt


T = 10000

if __name__ == "__main__":
	# func = BinaryString.get_one_count
	# string = BinaryString('110011')
	# print(type(BinaryString.get_one_count))
	# print(func(string))

	strings = [BinaryString() for _ in range(T)]
	# for string in strings:
	# 	print(string)

	cnts = [string.get_one_count() for string in strings]
	cnts.sort()
	# print(cnts)

	x = list(range(0, length + 1))
	y = [0] * (length + 1)

	cur = 0
	for i in x:
		while cur < T and cnts[cur] <= i:
			cur += 1

		y[i] = cur / T

	plt.plot(x, y)
	plt.show()