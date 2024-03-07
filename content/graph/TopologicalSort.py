# Alternative Topological Sort algorithm
from collections import deque
def altTopSort(g):
	inEdges = [0 for _ in range(len(g))]
	for v in range(len(g)):
		for a in g[v]:
			inEdges[a] = inEdges[a] + 1
	startNodes = []
	for v in range(len(g)):
		if inEdges[v] == 0:
			startNodes.append(v)
	path = []
	while startNodes:
		origin = startNodes.pop(0)
		path.append(origin)
		for a in g[origin]:
			inEdges[a] = inEdges[a] - 1
			if inEdges[a] == 0:
				startNodes.append(a)


