from ring import *
import argparse

def s1(k, x, n):
	try :
		ans = RingInt(n, 1)
		num = RingInt(n, 1)
		den = RingInt(n, 1)
		
		for i in range(1, k):
			den = den * RingInt(n, i)
			num = num * RingInt(n, x)
			ans = ans + num/den

		return ans

	except :
		return "UNDEFINED"

def s2(k, x, n):
	try :
		ans = RingInt(n, 1)
		fact = [RingInt(n, 1)]				# Stores factorials of numbers

		for i in range(1, x+k):
			fact.append(fact[i-1]*RingInt(n, i))

		for i in range(1, k):
			curterm = RingInt(n, 0)
			for j in range(i+1):
				curterm += fact[x+i] / (fact[j] * fact[x+i-j])
			ans = ans * curterm

		return ans

	except:
		return "UNDEFINED"

def s3(k, x, n):
	try :
		ans = RingInt(n, 1)
		
		for i in range(2, k+1):
			ans = ans + (RingInt(n, i)**x)

		return ans

	except:
		return "UNDEFINED"

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-in', type=str, required=True)
my_parser.add_argument('-out', type=str, required=True)

args = vars(my_parser.parse_args())

inpFile = open(args['in'], 'r')
outFile = open(args['out'], 'w')
lines = inpFile.readlines()

for line in lines:
	k, x, n, s = map(int, line.split())

	if s == 1:
		ans = s1(k, x, n)
	elif s == 2:
		ans = s2(k, x, n)
	else:
		ans = s3(k, x, n)

	outFile.write(str(ans) + '\n')

inpFile.close()
outFile.close()




