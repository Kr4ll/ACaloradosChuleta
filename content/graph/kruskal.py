	def find(parent, i): 
		if parent[i] != i: 
			parent[i] = find(parent, parent[i]) 
		return parent[i] 

	def union(parent, rank, x, y): 


		if rank[x] < rank[y]: 
			parent[x] = y 
		elif rank[x] > rank[y]: 
			parent[y] = x 

		else: 
			parent[y] = x 
			rank[x] += 1
			
	def KruskalMST(g,nodes): 

		result = [] 
		i = 0
		e = 0

		# sort by weight 
		g = sorted(g, key=lambda item: item[2]) 

		parent = [] 
		rank = [] 

		# Create V subsets with single elements 
		for node in range(0, nodes): 
		    parent.append(node) 
		    rank.append(0) 

		# Number of edges to be taken is less than to V-1 
		while e < nodes - 1: 

		    u, v, w = g[i] 
		    i = i + 1
		    x = find(parent, u) 
		    y = find(parent, v) 


		    if x != y: 
		        e = e + 1
		        result.append([u, v, w]) 
		        union(parent, rank, x, y) 
		    # Else discard the edge 

		minimumCost = 0
		for u, v, weight in result: 
		    minimumCost += weight 

