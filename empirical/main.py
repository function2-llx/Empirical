from binary_string import BinaryString
from rand_string import rand_string, length
from matplotlib import pyplot as plt
from empirical_plotter import EmpiricalPlotter

T = 10000

if __name__ == "__main__":
	strings = [BinaryString() for _ in range(T)]
	data = [string.get_one_count() for string in strings]
	plotter = EmpiricalPlotter(data)
	plotter.plot()
