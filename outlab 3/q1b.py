from ring import *
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-m', type=str, required=True)

args = vars(my_parser.parse_args())
inpFile = open(args['m'], 'r')

lines = inpFile.readlines()			# list of lines of file
n = int(lines[0])

corrupted = False

for line in lines:
	parts = line.split('$')
	for part in parts:
		if part.find('#') == -1:
			continue
		
		arrs = part.split('#')			# array of two strings: "(a1,a2,..)" and "(b1,b2,..)"
		if len(arrs) != 2:
			continue

		try:							# checking if indeed the strings are of expected form
			aray1 = list(map(int, arrs[0][1:-1].split(',')))	# aray1 stores [a1, a2, ..]
			aray2 = list(map(int, arrs[1][1:-1].split(',')))	# aray2 stores [b1, b2, ..]
		except ValueError :
			continue

		ans = RingInt(n, 0)
		for i in range(0, len(aray1)) :
			if aray1[i] < 0 or aray1[i] >= n:
				corrupted = True
				break
			ans += RingInt(n, i+1) * RingInt(n, aray1[i])
		
		if ans.value != 0 :
			corrupted = True
			break

		for i in range(0, len(aray2)) :
			if aray2[i] < 0 or aray2[i] >= n:
				corrupted = True
				break
			ans += RingInt(n, i+1) * RingInt(n, aray2[i])
		
		if ans.value != 0 :
			corrupted = True
			break

	if corrupted:
		break

if corrupted:
	print("CORRUPTED")
else:
	print("OK")

inpFile.close()