import copy
from math import inf

def esFactible(laberinto,f,c):
    if f>=0 and f<len(laberinto) and c>=0 and c<len(laberinto[0]):
        return laberinto[f][c] == 0
    else:
        return False

def esSolucion(laberinto,f,c):
    return f == len(laberinto)-1 and c == len(laberinto)-1

def esMejor(sol1,sol2):
    return sol1[len(sol1)-1][len(sol1[0])-1] < sol2[len(sol2)-1][len(sol2[0])-1]

def salirDelLaberinto(laberinto,mejorSol,f,c,k):
    if esSolucion(laberinto,f,c):
        if esMejor(laberinto,mejorSol):
            mejorSol = copy.deepcopy(laberinto)
    else:
        desplazamientos=[[1,0],[0,1],[-1,0],[0,-1]]
        i = 0
        while not esSol and i < len(desplazamientos):
            if esFactible(laberinto,f+desplazamientos[i][0],c+desplazamientos[i][1]):
                laberinto[f+desplazamientos[i][0]][c+desplazamientos[i][1]] = k
                mejorSol = salirDelLaberinto(laberinto,mejorSol,f+desplazamientos[i][0],c+desplazamientos[i][1],k+1)
                laberinto[f + desplazamientos[i][0]][c + desplazamientos[i][1]] = 0
            i += 1
    return mejorSol
