import math

primeraF = list(map(int, input().split()))


# Dominio: Recibe una matriz.
# Codominio: La copia de la matriz recibida.
def copia(matriz):
    matrizNueva = []
    for i in range(len(matriz)):
        fila = []
        for j in range(len(matriz[i])):
            fila.append(matriz[i][j])
        matrizNueva.append(fila)
    return matrizNueva


# Dominio: un sudoku resuelto
# Codominio: el sudoku con el formato deseado
def imprimir(sudoku):
    for i in range(len(sudoku)):
        print(*sudoku[i])


# Dominio: Un sudoku y una posicion (pos[0]=fila y pos[1]=columna).
# Codominio: Un vector con las posibilidades de la casilla del sudoku.
def obtenerPosibilidades(sudoku, pos):
    posibilidades = []
    for num in range(1, len(sudoku) + 1):
        if not contradiccion(sudoku, pos[0], pos[1], num):
            posibilidades.append(num)
    return posibilidades


# Dominio: Recibe un sudoku.
# Codominio: Retornar una fila ([0]), columna([1]) y un vector con las posibilidades([2]).
def obtenerCasillaMenosPosibilidades(sudoku):
    menorPosibilidades = False
    casillaVacia = False
    for x in range(len(sudoku)):
        for y in range(len(sudoku[x])):
            if sudoku[x][y] == 0:
                casillaVacia = True
                posibilidades = obtenerPosibilidades(sudoku, (x, y))
                if len(posibilidades) == 1:
                    return (x, y, posibilidades)
                elif not menorPosibilidades or len(posibilidades) < len(menorPosibilidades[2]):
                    menorPosibilidades = (x, y, posibilidades)
    if casillaVacia:
        return menorPosibilidades


# Dominio: El sudoku, su tamaño, la posición i,j de un 0 y el número que se planea insertar.
# Codominio: True si el número se repite en la región del 0 y False si no
def contradiccionRegion(sudoku, tam, i, j, num):
    subcuad = int(math.sqrt(tam))
    inicioI = (i // subcuad) * subcuad
    finalI = inicioI + subcuad
    inicioJ = (j // subcuad) * subcuad
    finalJ = inicioJ + subcuad
    for fil in range(inicioI, finalI):
        for col in range(inicioJ, finalJ):
            if (sudoku[fil][col] == num):
                return True
    return False


# Dominio: El sudoku, la posición i,j de un 0 y el número que se planea insertar ahí.
# Codominio: True si "num" se repite en la fila, columna o región y False si no se
# repite en ninguna.
def contradiccion(sudoku, i, j, num):
    tam = len(sudoku)
    for fila in range(tam):
        if (fila != i and sudoku[fila][j] == num):
            return True
    for col in range(tam):
        if (col != j and sudoku[i][col] == num):
            return True
    if (contradiccionRegion(sudoku, tam, i, j, num)):
        return True
    return False


# Dominio: la matriz del sudoku
# Codominio: True si no hay ningún 0 en la matriz, False si hay alguno.
def esSolucion(matriz):
    tam = len(matriz)
    for fila in range(tam):
        for col in range(tam):
            if (matriz[fila][col] == 0):
                return False
    return True


# Dominio: Recibe un sudoku sin resolver.
def resolverSudoku(sudoku):
    pila = []
    pila.append(list(sudoku))
    resuelto = False
    while (len(pila) > 0 and not resuelto):
        tope = pila.pop()
        posibilidades = obtenerCasillaMenosPosibilidades(tope)
        if esSolucion(tope):
            imprimir(tope)
            resuelto = True
        elif len(posibilidades[2]) == 1:  # Agrega a la pila el sudoku con la única posibilidad
            tope[posibilidades[0]][posibilidades[1]] = (posibilidades[2])[0]
            pila.append(tope)
        else:  # Más de una posibilidad, agrega los hijos a la pila
            for posibilidad in posibilidades[2]:
                hijo = copia(tope)
                hijo[posibilidades[0]][posibilidades[1]] = posibilidad
                pila.append(hijo)


# Dominio: números que representan las filas de un sudoku sin resolver
# Codominio: el sudoku representado como una matriz
def entrada(primeraF):
    sudoku = [primeraF]
    for filas in range(len(primeraF) - 1):
        fila = list(map(int, input().split()))
        sudoku.append(fila)
    resolverSudoku(sudoku)


entrada(primeraF)
