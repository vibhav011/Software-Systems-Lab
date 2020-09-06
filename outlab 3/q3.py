import argparse
from collections import Counter

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-ca', type=str, required=True)
my_parser.add_argument('-ch', type=str, required=True)

args = vars(my_parser.parse_args())

cand = open(args['ca'], 'r').readlines()
child = open(args['ch'], 'r').readlines()

M = int(cand[0])
types = list(map(int, cand[1].split()))

freq = Counter()						# counter to store frequency of each type in the shop
for cnd in types:
	freq[cnd] += 1

N = int(child[0])

demand = {}						# dict which stores candy type vs list of money offerred
for i in range(1, N+1):
	t, m = map(int, child[i].split())
	if t in demand.keys():
		demand[t].append(m)
	else:
		demand[t] = [m]

ans = 0
for tp in demand:
	if tp not in freq.keys():
		continue
	demand[tp].sort(reverse = True)
	temp = 0
	for i in range(min(freq[tp], len(demand[tp]))):
		temp += demand[tp][i]
	ans += temp

print(ans)


