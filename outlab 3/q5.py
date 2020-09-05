def rotate(m):
	n = len(m)
	ans = []
	for i in range(n):
		final = []
		for j in range(n):
			final.append(m[n-j-1][i])
		ans.append(final)
	return ans