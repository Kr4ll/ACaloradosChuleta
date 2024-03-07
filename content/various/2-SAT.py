# Dado unas clausulas en formato CNF obtener los posibles valores que satisfagan las clusulas.
from collections import defaultdict 
# Constants
MAX = 100000 
# Data structures used to implement Kosaraju's Algorithm
adj = defaultdict(list)
adj_inv = defaultdict(list)
visited = [False] * (MAX + 1)
visited_inv = [False] * (MAX + 1)
s = []
scc = [0] * (MAX + 1)
counter = 1
 
# Function to add edges to form the original graph
def add_edges(a, b):
    adj[a].append(b)
 
# Function to add edges to form the inverse graph
def add_edges_inverse(a, b):
    adj_inv[b].append(a)
 
# STEP 1 of Kosaraju's Algorithm - DFS on the original graph
def dfs_first(u):
    if visited[u]:
        return
 
    visited[u] = True
 
    for neighbor in adj[u]:
        dfs_first(neighbor)
 
    s.append(u)
 
# STEP 2 of Kosaraju's Algorithm - DFS on the inverse graph
def dfs_second(u):
    if visited_inv[u]:
        return
 
    visited_inv[u] = True
 
    for neighbor in adj_inv[u]:
        dfs_second(neighbor)
 
    scc[u] = counter
 
# Function to check 2-Satisfiability
def is_2_satisfiable(n, m, a, b):
    global counter  # Declare counter as a global variable
 
    # Adding edges to the graph
    for i in range(m):
        if a[i] > 0 and b[i] > 0:
            add_edges(a[i] + n, b[i])
            add_edges_inverse(a[i] + n, b[i])
            add_edges(b[i] + n, a[i])
            add_edges_inverse(b[i] + n, a[i])
        elif a[i] > 0 and b[i] < 0:
            add_edges(a[i] + n, n - b[i])
            add_edges_inverse(a[i] + n, n - b[i])
            add_edges(-b[i], a[i])
            add_edges_inverse(-b[i], a[i])
        elif a[i] < 0 and b[i] > 0:
            add_edges(-a[i], b[i])
            add_edges_inverse(-a[i], b[i])
            add_edges(b[i] + n, n - a[i])
            add_edges_inverse(b[i] + n, n - a[i])
        else:
            add_edges(-a[i], n - b[i])
            add_edges_inverse(-a[i], n - b[i])
            add_edges(-b[i], n - a[i])
            add_edges_inverse(-b[i], n - a[i])
 
    # STEP 1 of Kosaraju's Algorithm - Traverse the original graph
    for i in range(1, 2 * n + 1):
        if not visited[i]:
            dfs_first(i)
 
    # STEP 2 of Kosaraju's Algorithm - Traverse the inverse graph
    while s:
        node = s.pop()
        if not visited_inv[node]:
            dfs_second(node)
            counter += 1
 
    # Check if there exist variables x and -x in the same SCC
    for i in range(1, n + 1):
        if scc[i] == scc[i + n]:
            print("The given expression is unsatisfiable.")
            return
 
    # No such variables x and -x exist in the same SCC
    print("The given expression is satisfiable.")
 
# Driver function to test the implementation
def main():
    # Number of variables, number of clauses
    n, m = 5, 7
 
    # Example CNF (x1+x2)*(x2'+x3)*(x1'+x2')*(x3+x4)*(x3'+x5)*(x4'+x5')*(x3'+x4)
    a = [1, -2, -1, 3, -3, -4, -3]
    b = [2, 3, -2, 4, 5, -5, 4]
 
    is_2_satisfiable(n, m, a, b)
 
if __name__ == "__main__":
    main()
