def inicializarSolucion(grafo):
    sol = [0] * grafo['n']
    return sol

def esFactible(grafo,sol,nodo,color):
    factible = True
    adyacenciaNodo = grafo['adyacencia'][nodo]
    i = 0
    while factible and i < len(adyacenciaNodo):
        if adyacenciaNodo[i] < nodo:
            factible = color != sol[adyacenciaNodo[i]]
        i += 1
    return factible

def esSolucion(nodo, grafo):
    return nodo >= grafo['n']


def coloreadoVA(grafo, m, sol, nodo):
    #if nodo >= grafo['n']:
    if esSolucion(nodo, grafo):
        esSol = True
    else:
        esSol = False
        color = 1
        while not esSol and color <= m:
            if esFactible(grafo, sol, nodo, color):
                sol[nodo] = color
                [sol, esSol] = coloreadoVA(grafo, m, sol, nodo + 1)
                if not esSol:
                    sol[nodo] = 0
            color += 1
    return sol, esSol
