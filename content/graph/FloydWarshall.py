def floydWarshall(graph, n):
	dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
	for k in range(n):
		for i in range(n):
			for j in range(n):
				dist[i][j] = min(dist[i][j],
					dist[i][k] + dist[k][j])
					printSolution(dist, n)
def printSolution(dist, n):
	print("Following matrix shows the shortest distances\
	between every pair of vertices")
	for i in range(n):
		for j in range(n):
			if(dist[i][j] > 0x3f3f3a):
				print('INF\t', end=" ")
			else:
				print(f'{dist[i][j]}\t', end=' ')
			if j == n-1:
				print()
