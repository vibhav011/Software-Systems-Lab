import argparse
import pandas as pd
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--data', type=str, required=True)

args = parser.parse_args()

data = pd.read_csv(args.data)
print(data.head())

# df = pd.DataFrame({
#     'name':['john','mary','peter','jeff','bill','lisa','jose'],
#     'age':[23,78,22,19,45,33,20],
#     'gender':['M','F','M','M','M','F','M'],
#     'state':['california','dc','california','dc','california','texas','texas'],
#     'num_children':[2,0,0,3,2,1,4],
#     'num_pets':[5,1,0,5,2,2,3]
# })

for ind in data.index:
	print(data['REG'][ind])
	if ind == 10:
		break

# df.plot(kind='scatter',x='num_children',y='num_pets',color='red')
# plt.savefig('instance1.png')