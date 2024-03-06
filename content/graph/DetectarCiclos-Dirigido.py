 def isCyclicUtil(g, v, visited, recStack):
 
        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True
 
        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in g[v]:
            if visited[neighbour] == False:
                if isCyclicUtil(g, neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
 
        # The node needs to be popped from
        # recursion stack before function ends
        recStack[v] = False
        return False
 
    # Returns true if graph is cyclic else false
    def isCyclic(g):
    	n=len(g)
        visited = [False] * n
        recStack = [False] * n
        for node in range(0,n):
            if visited[node] == False:
                if isCyclicUtil(g, node, visited, recStack) == True:
                    return True
        return False
