# Ejercicio Trapping Rain Water
# link: https://leetcode.com/problems/trapping-rain-water/
import numpy as np
def Rain_Water(lista):
    ''' Funcion que evalua cuanta agua queda represada en los espacios entre cubos,
    el planteamiento se hace mediante la completacion de una matriz,
    columnas: longitud de la lista ingresada, fila: longitud valor mas grande de la lista,
    se rellenan con 1 si hay muro, en caso contrario con ceros, luego el programa recorre
    fila por fina hasta encontrar un "0", luego de esto se evalua si hay muro a la derecha
    y a la izquierda de dicho 0, en caso de que no se rellena con cualquier numero para representar
    que no contiene agua, finalmente se suma la cantidad de ceros por cada fila y esa es la cantidad
    final de agua que queda represada'''
    # detalle de ultima hora, importo numpy para reducir procesos en memoria, se trabo el
    # programa con un ejemplo muy grande
    if lista == []: # solo por si la lista esta vacia
        return 0
    lista = np.array(lista) # convierto la lista en un array de numpy
    arr = np.empty(shape = (max(lista), len(lista)), dtype = "i")    # creo una matriz vacia que voy a llenar mas adelante                                                                
    for i in range(max(lista)):        # recorro fila por fila de la matriz
        if i > 0: # a partir de la 2da fila voy disminuyendo a la lista
            lista -= 1
        arr[i] = (list(map(lambda x: 0 if x <= 0 else 1, lista))) # utilizo map para filtar los 0 y 1 si hay muro
        ceros = np.where(arr[i] == 0)       # utilizo la funcion where de numpy para encontrar los indices de los 0
        ochos = list(filter(lambda index: not(1 in arr[i][index::] and 1 in arr[i][index::-1]), ceros[0]))  # filtro los 0 si no hay  muro a ambos lados
        arr[i].put(ochos, 8)    # reescribo los 0s con 8 donde no hay agua ni muros
    for a in arr[::-1]:
        print(a)
    return (len(arr[arr == 0])) # retorno la cantidad de agua represada entre los cubos

#Ejemplos
Rain_Water([0,1,0,2,1,0,1,3,2,1,2,1])
Rain_Water([4,2,0,3,2,5])
Rain_Water([])
