# Ejercicio extraido de: https://www.aceptaelreto.com/problem/statement.php?id=104
# Ejercicio de Nodos y arboles binarios, o de recursividad
# mirar imagen anclada

def en_equilibrio(pi,di,pd,dd) -> bool:
    """ Funcion que evalua el equilibrio del movil
    Parameters:
        pi: int
            peso del movil_izquierdo, 0 si tiene un submovil anclado
        di: int
            longitud de la barra que sostiene a pi
        pd: int 
            peso del movil_derecho, 0 si tiene un submovil anclado  
        dd: int
            longitud de la barra que sostiene a pd
    Return: 
        True si esta en equilibrio
        False si esta desequilibrado
    """
    if pi < 0 or pd < 0: return False # si es negativo desde ya, esta desequlibrado y no necesito evaluar
    if pi*di == pd*dd:
        return True
    return False

def movil(pi,di,pd, dd):
    """ Funcion recursiva que me retorna un entero diferente de -1 si el movil esta
        equilibrado
    Parameters:
        pi: int
            peso del movil_izquierdo, 0 si tiene un submovil anclado
        di: int
            longitud de la barra que sostiene a pi
        pd: int 
            peso del movil_derecho, 0 si tiene un submovil anclado  
        dd: int
            longitud de la barra que sostiene a pd
    Return: 
        -1 si el movil esta desequilibrado, un entero ! de -1 indicando equilibrio
    """
    if pi == 0: 
        lado1, peso1, lado2, peso2 = tuple(map(int,input().split())) # entrada parseada a entero
        # entrada = input().split()
        # lado1 = int(entrada[1])
        # peso1 = int(entrada[0])
        # lado2 = int(entrada[3])
        # peso2 = int(entrada[2])
        pi = movil(peso1, lado1, peso2, lado2)
    if pd == 0: 
        lado1, peso1, lado2, peso2 = tuple(map(int,input().split())) # entrada parseada a entero
        # entrada = input().split()
        # lado1 = int(entrada[1])
        # peso1 = int(entrada[0])
        # lado2 = int(entrada[3])
        # peso2 = int(entrada[2])
        pd = movil(peso1, lado1, peso2, lado2)
    if en_equilibrio(pi, di, pd, dd):
        suma = pi+pd
        return suma
    else:
        return -1

while True: 
    entrada = input().split()
    lado1, peso1, lado2, peso2 = tuple(map(int,entrada)) # entrada parseada a entero
    # entrada = input().split()
    # lado1 = int(entrada[1])
    # peso1 = int(entrada[0])
    # lado2 = int(entrada[3])
    # peso2 = int(entrada[2])
    if entrada == ["0", "0", "0", "0"]: break
    salida = movil(peso1, lado1, peso2, lado2)
    if salida != -1: # si la salida es -1, el movil no esta en equilibrio
        print("SI")
    else:
        print("NO")


# EJEMPLOS:
"""
0 9 0 3
2 5 1 10
3 2 0 1
2 4 4 2
SI
-------
0 2 0 4
0 3 0 1
1 1 1 1
2 4 4 2
1 6 3 2
SI
------
"""
