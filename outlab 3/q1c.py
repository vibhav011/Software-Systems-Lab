from ring import *

class Series:

	def __init__(self, k, x, n):
		self.k = int(k)
		self.x = int(x)
		self.n = int(n)
		self.index = 0

	def __iter__(self):
		self.num = RingInt(self.n, 1)
		self.den = RingInt(self.n, 1)
		return self

	def __next__(self):
		if self.index >= self.k :
			raise StopIteration

		ans = self.num/self.den
		self.index += 1
		self.num *= RingInt(self.n, self.x)
		self.den *= RingInt(self.n, self.index)
		return ans


def main():

	in_str = str(input())
	in_list = in_str.split(' ')
	k, x, n = in_list[0], in_list[1], in_list[2]
	
	for ele in Series(k, x, n):
		print(ele)


if __name__=="__main__":
	main()

