 def isCyclicUtil(g, v, visited, parent):
        # Mark current node as visited and
        visited[v] = True
        # Recur for all neighbours
        # if any neighbour is visited and in
        for neighbour in g[v]:
            if visited[neighbour] == False:
                if isCyclicUtil(g, neighbour, visited, v) == True:
                    return True
             elif parent != i:
                return True
        # The node needs to be popped from
        # recursion stack before function ends
        recStack[v] = False
        return False
    # Returns true if graph is cyclic else false
    def isCyclic(g):
    	n=len(g)
        visited = [False] * n
        for node in range(0,n):
            if visited[node] == False:
                if isCyclicUtil(g, node, visited, -1) == True:
                    return True
        return False
