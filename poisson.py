import scipy.stats as stats

k1 = stats.poisson.pmf(6, 10)
print("probability of not raining for 6 days: ", k1)

k2 = stats.poisson.pmf(12, 10) + stats.poisson.pmf(13, 10) + stats.poisson.pmf(14, 10)
print("probability of not raining for 12 - 14 days: ", k2)