import random

length = 200

def rand_string():
	return ''.join([str(random.randint(0, 1)) for _ in range(length)])

if __name__ == "__main__":
	pass
