import functools

def collapse(L):
	if type(L) == str:
		return L
	if len(L) == 1:
		return collapse(L[0])
	return functools.reduce(lambda x, y: collapse(x) + ' ' + collapse(y), L)

L = [ ["this","is"], [ ["an", "interesting", "python"], ["programming", "exercise."] ] ]
print(collapse(L))