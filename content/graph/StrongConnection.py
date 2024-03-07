 time=0
 def SCCUtil(g, u, low, disc, stackMember, st):
        # Initialize discovery time and low value
        disc[u] = time
        low[u] = time
        time += 1
        stackMember[u] = True
        st.append(u)
        # Go through all vertices adjacent to this
        for v in g[u]:
            # If v is not visited yet, then recur for it
            if disc[v] == -1:
                SCCUtil(v, low, disc, stackMember, st)
                low[u] = min(low[u], low[v])
            elif stackMember[v] == True:
                '''Update low value of 'u' only if 'v' is still in stack
                (i.e. it's a back edge, not cross edge).
                Case 2 (per above discussion on Disc and Low value) '''
                low[u] = min(low[u], disc[v])
        # head node found, pop the stack and print an SCC
        w = -1  # To store stack extracted vertices
        if low[u] == disc[u]:
            while w != u:
                w = st.pop()
                stackMember[w] = False
    # The function to do DFS traversal.
    # It uses recursive SCCUtil()
    def SCC(g):
 		     n=len(g)
        disc = [-1] * n
        low = [-1] * n
        stackMember = [False] * n
        st = []
        for i in range(0,n):
            if disc[i] == -1:
                SCCUtil(g, i, low, disc, stackMember, st)
