#  metodo de cifrado cesar, se pasa de parametro (texto y clave)
from time import sleep
abc = ("a", "b","c","d","e","f","g","h","i","j","k",
        "l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
abc = abc*2
def Cifrado(texto, llave):
    texto2 = texto.lower() 
    cifrado = ""
    for indice, letra in enumerate(texto2):
        if letra not in abc:
            cifrado += letra
        else:
            if texto[indice].isupper(): 
                cifrado += abc[abc.index(letra)+llave].upper()
            else:
                cifrado += abc[abc.index(letra)+llave]
    return cifrado
    
def Descifrar(texto, llave):
    texto2 = texto.lower() 
    cifrado = ""
    for indice, letra in enumerate(texto2):
        if letra not in abc:
            cifrado += letra
        else:
            if texto[indice].isupper(): 
                cifrado += abc[abc.index(letra,abc.index(letra)+1)-llave].upper()
            else:
                cifrado += abc[abc.index(letra,abc.index(letra)+1)-llave]
    return cifrado

def Mostrar():
    print("Presiona 1 ---- para Cifrar un Mensaje")
    print("Presiona 2 ---- para Descifrar un Mensaje")
    print("Presiona X ---- para Salir")

while True:
    Mostrar()
    opcion = input("Ingresa Tu opcion: ")
    sleep(2)
    if opcion == "1":
        texto = input("Ingresa tu texto a Cifrar: ")
        clave = int(input("Ingresa tu clave de cifrado: "))
        MensajeCifrado = Cifrado(texto, clave)
        print("Mensaje Cifrado: ",MensajeCifrado )
    elif opcion == "2":
        texto = input("Ingresa tu texto a Descifrar: ")
        clave = int(input("Ingresa tu clave de Descifrado: "))
        MensajeDescifrado = Descifrar(texto,clave)
        print("Mensaje Descifrado: ", MensajeDescifrado)
    elif opcion == "X":
        print("salida exitosa del programa".center(60, "-"))
        break
    else:
        print("Escribe bien imbecil")





