# Ejercicio: https://www.aceptaelreto.com/problem/statement.php?id=255&potw=1

def max_palindrome(word: str) -> int:
    """ Funcion que me retorna la longitud mayor del palindrome interno.
    Paremters:
        word: str
            palabra a buscar la lungitud de su mayor palindro interno
    Return
        len_mayor: int
            Longitud del mayor palindrome encontrado"""

    len_mayor = 1 # esta es la longitud minima
    bandera = False # bandera para acabar el ciclo
    # recorrer por fuerza bruta de mayor longitud a menor longitud por conviencia,
    #  ya que al encontrar un mayor valor inmediatamente acabo el ciclo
    #  porque es el palindrome mas grande
    for index in range(2,len(word)+1)[::-1]: 
        for iter_index in range(len(word)): # formo nuevas palabras de la longitud(index)
            if len(word[iter_index:]) < index: break # si la longitud es menor rompo el ciclo buscando uno de menor longitud
            N_word = word[iter_index:iter_index+index] # formo la nueva palabra
            len_palindrome = Len_Palindrome(N_word) # compruebo si es palindrome
            if len_palindrome > len_mayor:
                len_mayor = len_palindrome
                bandera = True
                break
        if bandera is True: break # compruebo si encontre la bandera
    return len_mayor


def Len_Palindrome(word: str) -> len:
    """Funcion para encontrar la longitud del palindrome
    Paremters:
        word: str
            palabra a buscar la lungitud de su mayor palindro interno
    Return
        len_word: int
            longitud del palindrome, si no lo es retorno 0.
    """
    if word == word[::-1]:
        len_word = len(word)
        return len_word
    return 0    
    
while True:
    word = input()
    len_max = max_palindrome(word)
    print(len_max)
