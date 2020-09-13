import csv
import numpy as np

days = []				# Mon, Tues, etc.

with open('./mumbai_data.csv') as csvfile:
	file_object = csv.reader(csvfile)
	file_object.__iter__().__next__()		# skips the header line
	for row in file_object:
		days.append(row[0])

with open('./mumbai_data.csv') as csvfile:
	data_lock = np.genfromtxt(csvfile, delimiter = ',')
	data_lock = data_lock[1:, 1:3]

with open('./mumbai_unlock.csv') as csvfile:
	data_unlock = np.genfromtxt(csvfile, delimiter = ',')
	data_unlock = data_unlock[1:, 1:3]

data_lock[:, 0] = data_lock[:, 1]/data_lock[:, 0]
data_unlock[:, 0] = data_unlock[:, 1]/data_unlock[:, 0]

with open('./info_combine.csv', 'w+') as csvfile:
	file_object = csv.writer(csvfile)
	file_object.writerow(['Day', 'Infected(UnLock)', 'Infected(Lock)', 'Positivity Rate(Lock)', 'Positivity Rate(UnLock)'])

	for i in range(7):
		file_object.writerow([days[i],
							  int(data_unlock[i, 1]),
							  int(data_lock[i, 1]),
							  round(data_lock[i, 0], 3),
							  round(data_unlock[i, 0], 3),
							])