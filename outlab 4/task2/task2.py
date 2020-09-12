import argparse
import pandas as pd
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--data', type=str, required=True)

args = parser.parse_args()

data = pd.read_csv(args.data)

instances = ['i-1.txt', 'i-2.txt', 'i-3.txt']
filenames = ['instance1.png', 'instance2.png', 'instance3.png']
algos = ['round-robin', 'ucb', 'kl-ucb', 'thompson-sampling']
ep_values = [0.2, 0.02, 0.002]

grouped = data.groupby(['instance'])

for (ins, fname) in zip(instances, filenames):
	df = grouped.get_group(ins)
	grped = df.groupby(['algorithm'])
	
	plt.figure()
	plt.xlabel('horizon')
	plt.ylabel('Regret')
	plt.title('Instance ' + ins[2] + ' - both axes in log scale')

	for algo in algos :
		grpByAlgo = grped.get_group(algo)
		uniqueHorizons = list(grpByAlgo['horizon'].unique())
		uniqueHorizons.sort()
		grpByHor = grpByAlgo.groupby(['horizon'])

		reg_mean = []

		for hor in uniqueHorizons :
			samples = grpByHor.get_group(hor).sample(n = 50)
			reg_mean.append(samples['REG'].mean())

		plt.loglog(uniqueHorizons, reg_mean)
	
	ep_groups = grped.get_group('epsilon-greedy').groupby('epsilon')

	for ep in ep_values :
		grpByEp = ep_groups.get_group(ep)
		uniqueHorizons = list(grpByEp['horizon'].unique())
		uniqueHorizons.sort()
		grpByHor = grpByEp.groupby(['horizon'])

		reg_mean = []

		for hor in uniqueHorizons :
			samples = grpByHor.get_group(hor).sample(n = 50)
			reg_mean.append(samples['REG'].mean())

		plt.loglog(uniqueHorizons, reg_mean)
	
	plt.legend(algos + ['epsilon-greedy with epsilon=' + str(ep) for ep in ep_values])
	plt.savefig(fname)
