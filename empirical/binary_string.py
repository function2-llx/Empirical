# length = 200
# consider 1

from .rand_string import rand_string
from copy import copy, deepcopy
from .mathlib import sqr


class BinaryString:
	def __init__(self, string=''):
		if not string:
			self.string = rand_string()
		else:
			self.string = copy(string)

		for c in self.string:
			if not c in '01':
				raise Exception('01 string required')

	def __str__(self):
		return self.string

	def get_one_count(self):
		cnt = 0
		for c in self.string:
			cnt += c == '1'

		return cnt

	def get_longest(self):
		ret, cur = 0, 0
		for c in self.string:
			if c == '0':
				cur += 1
			else:
				cur = 0

			if cur > ret:
				ret = cur

		return ret
	# return substrings length =5, 6 and <= 7
	def get_equal_five(self):
		cnt, cur = 0, 0
		for c in self.string:
			if c == '0':
				cur += 1
			else:
				cur = 0

			if cur >= 5:
				cnt += 1


		return cnt

	def get_equal_six(self):
		cnt, cur = 0, 0
		for c in self.string:
			if c == '0':
				cur += 1
			else:
				cur = 0

			if cur >= 6:
				cnt += 1


		return cnt

	def get_not_greater_seven(self):
		cnt, cur = 0, 0
		for c in self.string:
			if c == '0':
				cur += 1
			else:
				cur = 0

			cnt += min((cur, 7))

		return cnt

	def get_n(self):
		i = 0
		n = [0] * 4
		while i < len(self.string):
			n[int(self.string[i]) << 1 | int(self.string[i + 1])] += 1
			i += 2

		return n

	def get_X(self):
		n = self.get_n()
		ret = 0
		for x in n:
			ret += sqr(x - 25)

		return ret / 25
