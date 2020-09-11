import csv
import numpy as np

data = np.zeros((7, 4))

days = []				# Mon, Tues, etc.

with open('mumbai_data.csv') as csvfile:
	file_object = csv.reader(csvfile)
	file_object.__iter__().__next__()		# skips the header line
	i = 0
	for row in file_object:
		days.append(row[0])
		for j in [0, 1, 2, 3] :
			data[i, j] = row[j+1]
		i += 1

data[:, 1] /= data[:, 0]		# test positivity rate
data[:, 0] /= 20.4				# tests per million

with open('transformed.csv', 'w+') as csvfile:
	file_object = csv.writer(csvfile)
	file_object.writerow(['Day', 'Tests', 'Infected', 'Recovered', 'Deceased'])

	for i in range(7):
		file_object.writerow([days[i],
							  int(round(data[i, 0])),
							  round(data[i, 1], 3),
							  int(data[i, 2]),
							  int(data[i, 3])
							])



