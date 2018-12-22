from scipy.special import gamma
from scipy.integrate import quad
from numpy import exp
from numpy.random import binomial
from scipy import stats

def sqr(x):
    return x * x

def gamma_distribution(x, alpha, lambda_):
    if x < 0:
        return 0
    
    return quad(lambda t: (t ** (alpha - 1)) * (lambda_ ** alpha) * exp(-lambda_ * t), 0, x)[0] / gamma(alpha)

def chi_square_distribution(x, n):
    return gamma_distribution(x, n / 2, 0.5)

def binomial_distribution(k, n, p):
    if (k < 0):
        return 0
    
    if (k > n):
        return 1

    ret = 0
    for i in range(k):
        ret += stats.binom.pmf(i, n, p)

    return ret