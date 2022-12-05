# Bernoulli Distribution

# p(x) = {p if k =1}
# p(x) = {1-p  if k=0}

# Here the parameter is p
import warnings
warnings.filterwarnings("ignore")
import scipy
from scipy.stats import bernoulli
import matplotlib.pyplot as plt
# parameters for bernoulli distribution
p = 0.3
# create random variable
random_variable = bernoulli(p)

# Binomial Distribution

from scipy.stats import binom
import matplotlib.pyplot as plt
# parameters for binomial distribution
n = 10
p = 0.3
# create random variable
random_variable = binom(n, p)
# compute probability mass function
x = scipy.linspace(0,10,11)
# plot
plt.figure(figsize=(12, 8))
plt.vlines(x, 0, random_variable.pmf(x))
plt.show()


# Poisson Distribution

from scipy.stats import poisson
import matplotlib.pyplot as plt
# parameters for bernoulli distribution
lambda_ = 0.1
# create random variable
random_variable = poisson(lambda_)
# compute probability mass function
x = scipy.linspace(0,5,11)
# plot
plt.figure(figsize=(12, 8))
plt.vlines(x, 0, random_variable.pmf(x))
plt.show()

# Gaussian Distribution

from scipy.stats import norm
import matplotlib.pyplot as plt
import scipy
# create random variable
random_variable = norm()
# compute probability mass function
x = scipy.linspace(-5,5,20)
# plot
plt.figure(figsize=(12, 8))
plt.vlines(x, 0, random_variable.pdf(x))
plt.show()


