def mochilaVA(solucion, mejorSol, datos, k):
    if esSolucion(solucion, datos):
        mejorSol = mejor(mejorSol, solucion)
    else:
        for i in range(k, datos['N']):
            if esFactible(solucion, datos, i):
                solucion = asignar(solucion, i, datos)
                mejorSol = mochilaVA(solucion, mejorSol, datos, i)
                solucion = borrar(solucion, i, datos)
    return mejorSol
