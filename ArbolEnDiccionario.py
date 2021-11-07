# arboles binarios dentro de diccionarios

# me entra una lista completa de los datos mapeados en foma de lista entera, Ej: [[0 2 5 4] [1 2 3 4] [3 8 0 2]]
# la funcion me retorna una lista de listas que contienen los submoviles de cada movil
def Sub_dividir_moviles(lista_mapeada: list[list]) -> list[list[list]]: 
    """Entra una lista de listas completa de los datos mapeados en foma de lista entera,
         Ej: [[0 2 5 4] [1 2 3 4] [3 8 1 5]]
        la funcion me retorna una lista de lista de listas que contienen los submoviles de cada movil.
        salida del Ejemplo: [ [ [0 2 5 4][1 2 3 4] ] , [[3 8 1 5]] ]
    Parameters:
        lista_mapeada: list
            lista de lista completa con los datos convertidoa
    Return:
        lista_final: list[list[list]]
            lista de lista de listas con los submoviles que conforman cada movil
  """
    lista_final = [[]]
    espera = 1
    index = 0
    for movil in lista_mapeada:
        lista_final[index].append(movil)
        espera += movil.count(0) - 1
        if espera == 0: 
            lista_final.append([])
            index += 1
            espera = 1
    lista_final.pop()
    return lista_final

def formar_movil(lista): # retornar un diccionario lleno con sus subregistros, la lista de salida se omite
    lado1 = lista[0][1]
    peso1 = lista[0][0]
    lado2 = lista[0][3]
    peso2 = lista[0][2]
    lista_final = {}

    if peso1 == 0 and peso2 == 0: 
        valor,lista = formar_movil(lista[1:])
        lista_final[lado1] = valor 
        if lado1 == lado2: lado2 = float(lado2)+0.1
        valor,lista = formar_movil(lista[1:])
        lista_final[lado2] = valor

    else:
        if peso1 == 0:
            valor,lista = formar_movil(lista[1:])
            lista_final[lado1] = valor
            if lado1 == lado2: lado2 = float(lado2)+0.1
            lista_final[lado2] = peso2

        elif peso2 == 0:
            valor,lista = formar_movil(lista[1:])
            lista_final[lado1] = peso1
            if lado1 == lado2: lado2 = float(lado2)+0.1
            lista_final[lado2] = valor

        else:

            lista_final[lado1] = peso1
            if lado1 == lado2: lado2 = float(lado2)+0.1 # por recursividad para no tener claves iguales, luego solo redonde por debajo y ya
            lista_final[lado2] = peso2

    return lista_final,lista
    
Lista_moviles = []
while True: 
    moviles = input().split()
    if moviles == ["0", "0", "0", "0"]: break
    Lista_moviles += [list(map(int, moviles))] # mapeo de datos enteros

Lista_moviles = Sub_dividir_moviles(Lista_moviles)
lista_movil = []
for movil in Lista_moviles:
    dic = formar_movil(movil)[0]
    lista_movil.append(dic)

# probar salida con json
import json
with open("datos.json", "w") as file:
    json.dump(lista_movil, file, indent=4)
    

# lo mismo de arriba pero menos especifico
# def insertar(lista):

#     lado1 = lista[0][1]
#     peso1 = lista[0][0]
#     lado2 = lista[0][3]
#     peso2 = lista[0][2]

#     if peso1 == 0 and peso2 == 0: 
#         # hay conflicto para encontrar el inicio del otro lado
#         lista_final = {lado1: insertar(lista[1:]), lado2: insertar(lista[1:])} 
#     else:
#         if peso1 == 0:
#             valor,lista = str(insertar(lista[1:]))
#             lista_final = {lado1: insertar(lista[1:]), lado2: peso2}
#         elif peso2 == 0:
#             lista_final = {lado1: peso1, lado2: insertar(lista[1:])}
#         else:
#             lista_final = {lado1: peso1, lado2: peso2}
    
#     return lista_final,lista
