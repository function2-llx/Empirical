from order.normal_set import NormalSet
from empirical.empirical_plotter import EmpiricalPlotter

T = 100000

if __name__ == "__main__":
	normals = [NormalSet() for _ in range(T)]
	
	for order in (1, 20, 50, 51):
		data = [n.get_order(order) for n in normals]
		plotter = EmpiricalPlotter(data, 'X(' + str(order) + ')')
		plotter.plot()
