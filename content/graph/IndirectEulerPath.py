 def isConnected(g):
 		n=len(g)
        # Mark all the vertices as not visited
        visited = [False]*(n)
        #  Find a vertex with non-zero degree
        for i in range(n):
            if len(g[i]) != 0:
                break
        # If there are no edges in the graph, return true
        if i == n-1:
            return True
        # Start DFS traversal from a vertex with non-zero degree
        DFSUtil(i, visited)
        # Check if all non-zero degree vertices are visited
        for i in range(n):
            if visited[i] == False and len(g[i]) > 0:
                return False
        return True
    '''The function returns one of the following values
       0 --> If graph is not Eulerian
       1 --> If graph has an Euler path (Semi-Eulerian)
       2 --> If graph has an Euler Circuit (Eulerian)  '''
    def isEulerian(g):
    	n=len(g)
        # Check if all non-zero degree vertices are connected
        if isConnected() == False:
            return 0
        else:
            # Count vertices with odd degree
            odd = 0
            for i in range(n):
                if len(g[i]) % 2 != 0:
                    odd += 1
            '''If odd count is 2, then semi-eulerian.
            If odd count is 0, then eulerian
            If count is more than 2, then graph is not Eulerian
            Note that odd count can never be 1 for undirected graph'''
            if odd == 0:
                return 2
            elif odd == 2:
                return 1
            elif odd > 2:
                return 0
