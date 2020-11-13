import requests
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

init = (requests.get('https://api.covid19india.org/csv/latest/case_time_series.csv').text).split('\n')
data = [init[i].split(',') for i in range(len(init))]

for i in range(len(data)):
	if data[i][0].strip() == "15 April":
		loc = i
		break

y = np.array([float(data[i][7])/float(data[i-1][7]) for i in range(loc, len(data))])
x = np.arange(1, len(data)-loc+1)

plt.scatter(x, y, s = 15, c='red', label="original data")

slope, intercept, a, b, c = stats.linregress(x, y)
ans = int(np.ceil((1-intercept)/slope))

xx = np.linspace(1, ans+10)
yy = xx*slope+intercept

plt.plot(xx, yy, 'b', label="regressed data")
plt.xlabel('t')
plt.ylabel('H(t)')
plt.title("covid19india")
plt.legend()
plt.savefig("covid.png")
plt.close()

print(ans)