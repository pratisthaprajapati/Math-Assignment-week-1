import numpy as np


ages_of_offenders = np.array([11, 12, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 22, 22, 22, 22, 23, 23, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 29, 30, 31, 34, 36, 39, 43, 46, 50, 54, 59, 67])

median = np.median(ages_of_offenders)

mode = np.unique(ages_of_offenders)[np.argmax(np.bincount(ages_of_offenders))]

first_quartile = np.percentile(ages_of_offenders, 25)
third_quartile= np.percentile(ages_of_offenders, 75)


p10 = np.percentile(ages_of_offenders, 10)
p95 = np.percentile(ages_of_offenders, 95)


print("your median is:", median)
print("your mode is:", mode)
print("The value of Q1 is:", first_quartile)
print("The value of Q3 is:", third_quartile)
print("The value of P10 is:", p10)
print("The value of P95 is:", p95)