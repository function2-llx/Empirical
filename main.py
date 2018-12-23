from empirical.binary_string import BinaryString
from empirical.rand_string import rand_string, length
from empirical.empirical_plotter import EmpiricalPlotter
from empirical.normal_set import NormalSet
from empirical.multi_empirical_plotter import MultiEmpiricalPlotter

T = 100000

if __name__ == "__main__":
    strings = [BinaryString() for _ in range(T)]
    funcs = {
        '1的个数': BinaryString.get_one_count,
        '最长1串': BinaryString.get_longest,
        '长度为5的1串': BinaryString.get_equal_five,
        '长度为6的1串': BinaryString.get_equal_six,
        '长度不超过7的1串': BinaryString.get_not_greater_seven,
        'X': BinaryString.get_X
    }

    for title in funcs:
        func = funcs[title]
        data = [func(string) for string in strings]
        plotter = EmpiricalPlotter(data, title)
        plotter.plot()

    normals = [NormalSet() for _ in range(T)]

    multi_plotter = MultiEmpiricalPlotter('次序统计量')
    
    for order in (1, 20, 50, 51):
        data = [n.get_order(order) for n in normals]
        if order in (1, 20, 50):
            multi_plotter.add(data)
        plotter = EmpiricalPlotter(data, 'X(' + str(order) + ')')
        plotter.plot()
        
    multi_plotter.plot()