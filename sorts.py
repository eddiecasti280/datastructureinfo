
def sequential_search(x, y):
	for value in range(len(x)):
		if(x[value]==y):
			return value
	return -1
 