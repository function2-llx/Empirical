from scipy.special import gamma
from scipy.integrate import quad
from numpy import exp

def sqr(x):
	return x * x

def gamma_distribution(x, alpha, lambda_):
	if x < 0:
		return 0
	
	return quad(lambda t: (t ** (alpha - 1)) * (lambda_ ** alpha) * exp(-lambda_ * t), 0, x)[0] / gamma(alpha)

def chi_square_distribution(x, n):
	return gamma_distribution(x, n / 2, 0.5)