import numpy as np

with open('./mumbai_data.csv') as csvfile:
	data = np.genfromtxt(csvfile, delimiter=',')
	data = data[1:, 1:]

f = lambda t : format(round(t, 3), '.3f')		# rounding function
mean = list(map(f, data.mean(axis=0)))
std = list(map(f, data.std(axis=0)))

cols = ['Tests', 'Infected', 'Recovered', 'Deceased']
heads = ['Field', 'Mean', 'Std. Dev.']

final = [heads] + list(zip(cols, mean, std))	# Merges all the data

for i in range(5):
	print ("{:<9}\t{:>10}\t{:>11}".format(*final[i]))