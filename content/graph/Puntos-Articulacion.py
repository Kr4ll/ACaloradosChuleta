def checkAP(u, v, children, p, ap, low, d):
	# u es la r a z del rbol y tiene al menos dos hijos
	if p[u] == -1 and children > 1:
		ap[u] = True
	# u no es r a z del rbol y tiene un hijo v
	if p[u] != -1 and low[v] >= d[u]:
		ap[u] = True
def artPointsRec(g, visited, v, ap, d, low, parent, t):
	visited[v] = True
	t += 1
	d[v] = t
	low[v] = t
	children = 0
	for adj in g[v]:
		if not visited[adj]:
			children += 1
			parent[adj] = v
			artPointsRec(g, visited, adj, ap, d, low, parent, t
			)
			if low[adj] < low[v]:
				low[v] = low[adj]
			checkAP(v, adj, children, parent, ap, low, d)
	elif adj != parent[v]:
		if low[v] > d[adj]:
			low[v] = d[adj]
def artPoints(g):
	n = len(g)
	visited = [False] * n
	d = [-1] * n # Iteraci n de descubrimiento
	low = [-1] * n # Descubrimiento m n i m o
	parent = [-1] * n # Padre de cada nodo
	ap = [False] * n # Nodos que son AP
	t = 0 # Iteraci n actual
	for v in range(1, n):
		if not visited[v]:
			artPointsRec(g, visited, v, ap, d, low, parent, t)
	return ap

