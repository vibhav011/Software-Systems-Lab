import csv
import numpy as np

data = np.zeros((7, 4))

with open('./mumbai_data.csv') as csvfile:
	file_object = csv.reader(csvfile)
	file_object.__iter__().__next__()		# skips the header line
	i = 0
	for row in file_object:
		for j in [0, 1, 2, 3] :
			data[i, j] = row[j+1]
		i += 1

f = lambda t : format(round(t, 3), '.3f')		# rounding function
mean = list(map(f, data.mean(axis=0)))
std = list(map(f, data.std(axis=0)))

cols = ['Tests', 'Infected', 'Recovered', 'Deceased']

print ("{:<9} {:>13} {:>12}".format('Field', 'Mean', 'Std. Dev.'))

for i in range(4) :
	print ("{:<9} {:>13} {:>12}".format(cols[i], mean[i], std[i]))