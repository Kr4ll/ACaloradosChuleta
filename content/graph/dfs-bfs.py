from collections import deque

def dfs(g, visited, v):
	q = deque()
	q.append(v)
	while q:
		aux = q.pop()
		if not visited[aux]:
			visited[aux] = True
		for adj in reversed(g[aux]):
			if not visited[adj]:
				q.append(adj)
#Recursivo
def dfsRec(g, visited, v):      
    visited[v] = True
    for adj in g[v]:
        if not visited[adj]:
            dfsRec(g,visited,adj)

def dfs(g):
    n = len(g) 
    visited = [False]*n  
    for v in range(1,n):   
        if not visited[v]:
            dfsRec(g,visited,v) 
            
            
def bfs(g, visited, v):
	q = deque()
	q.append(v)
	while q:
		aux = q.popleft()
		if not visited[aux]:
			print(aux, end=" ")
		visited[aux] = True
		for adj in g[aux]:
			if not visited[adj]:
				q.append(adj)
		



