from binary_string import BinaryString
from rand_string import rand_string, length
from matplotlib import pyplot as plt
from plotter import Plotter


T = 10000

if __name__ == "__main__":
	strings = [BinaryString() for _ in range(T)]
	plotter = Plotter(strings, BinaryString.get_one_count)
	plotter.plot()
	