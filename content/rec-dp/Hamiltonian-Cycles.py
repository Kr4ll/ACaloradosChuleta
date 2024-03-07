def hamiltonian_cycles(current, graph, visited, solution):
    for adjacent in graph[current]:
        if adjacent not in visited:  # esFactible
            visited.add(adjacent)
            solution.append(adjacent)
            if len(solution) == len(graph):  # esCasoBase
                if 0 in graph[adjacent]:  # esSolucion
                    print(solution)
            else:
                hamiltonian_cycles(adjacent, graph, visited, solution)
            solution.pop()
            visited.remove(adjacent)

