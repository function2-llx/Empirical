
# length = 200
# consider 0

class BinaryString:
	def __init__(self, string):
		self.string = string

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

			if cur >= 7:
				cnt += cur - 6

		return cnt

	def get_n(self):
		i = 0
		n = [0] * 4
		while i < len(self.string):
			n[int(self.string[i]) << 1 | int(self.string[i + 1])] += 1
			i += 2

		return n
