# dado la altura, retornar una matriz con las sublistas de los numeros que forman
# cada nivel en un triangulo de pascal 
# EJ: 1 -> [[1]]  
#  2 -> [[1], [1,1]] 
#  5-> [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# link Ejercicio: https://leetcode.com/problems/pascals-triangle/


def PascalTriangle(numRows: int) -> list[list]:
    """
    funcion que me retorna una lista de listas conformada por cada uno de las filas
    que puede tener un triangulo de pascal dada su altura, y llenando la lista de manera
    descendente.

    paramters:
        numRows: int
            Altura del triangulo de pascal al que le quiero hallar sus respectivas filas

    Return: 
        matriz: list[list]
            matriz que contiene las sublistas que indican la composicion fila por fila
            de del triangulod e pascal con altura (numRows)
    """
    if numRows == 1:
        return [[1]]
    inicio = [1]
    pascal = [1,1]
    listaFinal=[inicio, pascal]
    for i in range(2,numRows):
        variador = pascal
        pascal = [1,1]
        for j in range(1,len(variador)): # se inicia desde la posicion 1 de la lista
            valor = variador[j]+variador[j-1] # el valor agregado es indice j - indice j-1
            pascal.insert(j, valor)
        listaFinal += [pascal]

    return listaFinal
numrow = int(input("Ingresa la altura del triangulo: "))

print(PascalTriangle(numrow))
