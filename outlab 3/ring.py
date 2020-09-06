class RingInt :
	def __init__(self, c, v):
		c = int(c)
		v = int(v)

		if c < 1:
			raise ValueError("Characteristic must be a positive integer.")
		
		self.characteristic = c
		self.value = v%c

	def __str__(self):
		return str(self.value) + '[' + str(self.characteristic) + ']'

	def __add__(self, other):
		if self.characteristic != other.characteristic :
			raise ValueError("Characteristics are not equal.")
		
		return RingInt(self.characteristic, self.value+other.value)

	def __sub__(self, other):
		if self.characteristic != other.characteristic :
			raise ValueError("Characteristics are not equal.")
		
		return RingInt(self.characteristic, self.value-other.value)

	def __mul__(self, other):
		if self.characteristic != other.characteristic :
			raise ValueError("Characteristics are not equal.")
		
		return RingInt(self.characteristic, self.value*other.value)

	def __truediv__(self, other):
		if self.characteristic != other.characteristic :
			raise ValueError("Characteristics are not equal.")

		if other.value == 0:
			raise ValueError("Can't divide by 0.")

		gcd = self.ExtendedGCD(self.characteristic, other.value)

		if gcd[0] != 1:
			raise ValueError("Division not possible.")

		return RingInt(self.characteristic, self.value*gcd[2])

	def __pow__(self, v):
		v = int(v)

		reciproc = False
		
		if v < 0:
			v = -v
			reciproc = True

		ans = 1
		x = self.value
		while v > 0:
			if v%2 == 1:
				ans = (ans*x) % self.characteristic

			x = (x*x) % self.characteristic
			v = v//2

		if reciproc:
			return RingInt(self.characteristic, 1)/ans
		
		return RingInt(self.characteristic, ans)

	def __eq__(self, other):
		if self.characteristic != other.characteristic :
			raise ValueError("Characteristics are not equal.")

		return self.value == other.value

	def ExtendedGCD(self, a, b) :				# Assumption: a >= b
		if a%b == 0:
			return [b, 0, 1]
		ans = self.ExtendedGCD(b, a%b);
		return [ans[0], ans[2], ans[1] - ans[2] * (a//b)]



