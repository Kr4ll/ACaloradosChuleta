import random, sys
# Devuelve el mejor valor de los candidatos
def getBest(candidates, elemSet):
	bestValue = sys.maxsize
	best = 0
	for c in candidates:
		value = elemSet[c]
		if value < bestValue:
			bestValue = value
			best = c
	return best
	# Algoritmo voraz
def greedy(elemSet):
	candidates = set()
	n = len(elemSet)
	for i in range(n):
		candidates.add(i)
		sol = []
	while candidates:
		best = getBest(candidates, elemSet)
		candidates.remove(best)
		sol.append(best)

