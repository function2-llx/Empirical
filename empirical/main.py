from BinaryString import BinaryString
from rand_string import rand_string

if __name__ == "__main__":
	string = BinaryString(rand_string())
	print(string)
	print('positive = ', string.get_one_count())
	print('longest = ', string.get_longest())
	print('five = ', string.get_equal_five())
	print('six = ', string.get_equal_six())
	print('(<=) seven = ', string.get_not_greater_seven())
	print('n0, n1, n2, n3 = ', string.get_n())