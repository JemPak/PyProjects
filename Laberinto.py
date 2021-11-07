''' Dada la secuencia de donde se encuentra los muros del laberinto, la Entrada y la Respectiva salida
Contruir: 1 - Imprimir a escala el laberinto, ["X" = hay muro, " " = paso del camino, "E"= entrada, "S"=salida]...
          2 - Imprimir una lista con el recorrido que se hace de la Entrada a la Salida''' 
# Ayuda: https://aprendeconalf.es/docencia/python/retos/laberinto/

muro = ((0,3), (0,4),(0,5),(1,1),(1,5),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(3,4),(4,2),(4,3),(5,0),(5,2),(5,3),(5,5),(6,0),(6,3),(7,0),(7,1),(7,3),(7,4),(7,5))
Entrada = (7,2)
Salida = (6,5)
Columna_muro_alejado = sorted(muro, key=lambda x:x[1])[-1][1] 
ancho = max(Columna_muro_alejado,Entrada[1],Salida[1]) 
largo = max(muro[-1][0],Entrada[0],Salida[0]) 
lab = [[" " for j in range(ancho+1)] for i in range(largo+1)] 
for pared in muro:
    lab[pared[0]][pared[1]] = "X"   
lab[Entrada[0]][Entrada[1]] = "E"   
lab[Salida[0]][Salida[1]] = "S"     
for i in lab:
    print(i)

def BuscarCamino(lista : list, posicion : tuple):
    ''' Evaluo si la posicion es parte del camino o no, me pasan de parametro
    la fila y la posicion, si es camino entonces luego pongo "X" en esta posicion
    del laberinto para no volver a tomarlo mas adelante'''
    direccion = lista[posicion[1]]
    if direccion == ' ':
        lab[posicion[0]][posicion[1]] = "X"
        return [True,posicion, False]
    elif direccion == 'S':
        return [True,posicion,True]
    else:
        return [False,posicion,False]
    # except:
    #     return [False,posicion,False]

print("Tamaño del laberinto: ",ancho, largo) 
DirCamino = []
camino = Entrada
fin = False
while fin == False: 
    fila = camino[0]
    columna = camino[1]
    derecha = [False,(fila,columna+1), False] # lista (False, posicion si muevo derecha)
    izquierda = [False,(fila,columna-1), False] # lista (False, posicion si muevo izquierda)
    arriba = [False,(fila-1,columna), False]    # # lista (False, posicion si muevo arriba)
    abajo= [False, (fila+1,columna), False]     # # lista (False, posicion si muevo abajo)
    # miro los lados
    if columna == 0:
        derecha = BuscarCamino(lab[fila], derecha[1])
    elif columna == ancho:
        izquierda= BuscarCamino(lab[fila], izquierda[1])      
    else:
        derecha= BuscarCamino(lab[fila], derecha[1])
        izquierda= BuscarCamino(lab[fila], izquierda[1])
    # miro arriba y abajo
    if fila == 0:
        abajo = BuscarCamino(lab[fila+1], abajo[1])
    elif fila == largo:
        arriba = BuscarCamino(lab[fila-1], arriba[1])
    else:
        abajo= BuscarCamino(lab[fila+1], abajo[1])
        arriba = BuscarCamino(lab[fila-1], arriba[1])
    # agrego la direccion a la lista 
    if derecha[0]:
        DirCamino.append("derecha")
        camino = derecha[1]
    elif izquierda[0]:
        DirCamino.append("Izquierda")
        camino = izquierda[1]
    elif arriba[0]:
        DirCamino.append("Arriba")
        camino = arriba[1]
    else:
        DirCamino.append("Abajo")
        camino = abajo[1]
    #if (derecha[2] == True or izquierda[2] == True or arriba[2] == True or abajo[2] == True):
    if (derecha[2] or izquierda[2] or arriba[2] or abajo[2]) == True:
        fin = True
print(DirCamino)

''' Mas Ejemplos '''
# muro = ((0,3), (0,4),(0,5),(1,1),(1,5),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(3,4),(4,2),(4,3),(5,0),(5,2),(5,3),(5,5),(6,0),(6,3),(7,0),(7,1),(7,3),(7,4),(7,5))
# Entrada = (7,2)
# Salida = (6,5)
################################################################
# muro = ((0,0),(0,1),(1,0),(1,1),(1,3),(1,4),(2,0), (2,1), (2,3),(2,4), (3,3),(3,4), (4,1), (4,2), (4,3),(4,4))
# Entrada = (4,0)
# Salida = (0,4)
################################################################
# muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
# Entrada = (0,0)
# Salida = (4,4)
