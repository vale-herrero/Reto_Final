import random

def disponibles(y,n):
    columnas_disponibles = []
    for x in range(n):
        if(columna[x] or diagonal_izquierda[x+y] or diagonal_derecha[x-y+n-1]):
            continue
        columnas_disponibles.append(x)
    return columnas_disponibles

soluciones = []
for n in (4,5,6,7,8,9,10,15):
    n = n
    solucion = []

    columna = [False] * n
    diagonal_izquierda = [False] * (n * 2)  
    diagonal_derecha = [False] * (n * 2)

    while(len(solucion)!=n and n>3):
        solucion = []
        columna = [False] * n
        diagonal_izquierda = [False] * (n * 2)
        diagonal_derecha = [False] * (n * 2)

        for y in range(n):
            columnas_d = disponibles(y,n)
            if(columnas_d):
                x = random.choice(columnas_d)
            else:
                break
            
            columna[x] = diagonal_izquierda[x+y] = diagonal_derecha[x-y+n-1] = True
            solucion.append((x,y))
            
    solucion_problema = [ pos[1] for pos in sorted(solucion, key=lambda x: x[0])]
    soluciones.append(solucion_problema)

print(soluciones)
