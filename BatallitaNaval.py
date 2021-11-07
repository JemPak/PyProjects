#Indicaciones antes de ejecutar
#no colocar columna = 20 ya que se sale de rango
# para los nombres de barco solo poner acorazado, patrullero o destructor
# en posicion, poner solo vertical o horizontal para no dañarlo
# Lo mas dificil es ver como inicias el camino hacia el final, pero antes del fin ahí estas tú - JemPak

from copy import deepcopy as copia
#import numpy as np
llenar_tablas = lambda : [[" - " for i in range(20)] for k in range(20) ]  # forma una tabla vacia rapidamente
def llenar_posiciones(datos):
   for i in range(datos["NumeroBarcos"]):
      barco, valores, datos["tabla"] = llenar_Barco(datos["tabla"])
      datos["barcos"][barco] += [valores]
   return datos
  
def info_barco():
   barcos = { "acorazado": 3, "destructor": 4, "patrullero": 2}
   while True:
      tipoB = input("Tipo de barco a ubicar [ Acorazado-Destructor-Patrullero ]:\t" ).lower()
      if tipoB in barcos:
         casillas = barcos[tipoB]
      else:
         print("Escribe bien el tipo de barco imbecil")
         continue
      while True:
         try:
            fila, columna, orientacion = input("Ingresa Fila, Columna y Orientacion EJ( 7-3-v)" + ":\t\t\t").strip().split("-")
            if date_error(fila, columna, orientacion): # retorna true o false si la ubicacion es correcta
               return tipoB, casillas, int(fila)-1, int(columna)-1, orientacion
            continue
         except:
            print("Ubicacion Invalida, intenta nuevamente")

   
def llenar_Barco(tablas):
   barco, p, fila, columna, orientacion = info_barco()
   valores = []
   if orientacion == "v":
      for i in range(fila, fila+p):
         tablas[i][columna] = "| |"
         valores.append(str(i+1)+str(columna+1))
   else:
      for i in range(columna, columna+p):
         tablas[fila][i] = "| |"
         valores.append(str(fila+1)+str(i+1))
   return barco, valores, tablas


def disparar(barcos,jug,disparo, campo):
   texto = ""
   buques=("acorazado","patrullero","destructor")
   golpe = False
   for TipoB in buques:
      for barco in barcos[jug]["barcos"][TipoB]:
         if disparo["posicion"] in barco:
            golpe = True
            barco.remove(disparo["posicion"])
            if not barco: # si la tabla está vacía
               barcos[jug]["NumeroBarcos"] -= 1
               texto = "Has derribado un " + TipoB                  
            else:
               texto = "Has golpeado un barco"
            barcos["campo"][1], barcos["campo"][2]= tablero(barcos["campo"][1], barcos["campo"][2], disparo["fila"]-1, disparo["columna"]-1, campo, golpe)   
            print(texto, "\n")
            return barcos
   else:
      texto = "Disparo al agua .-."
      barcos["campo"][1], barcos["campo"][2] = tablero(barcos["campo"][1], barcos["campo"][2], disparo["fila"]-1, disparo["columna"]-1, campo, golpe)   
      print(texto, "\n")
      return barcos   
   
def tablero(tabla1, tabla2, filas=None, columnas=None, jugador=None, golpe=None):
   try:
      if jugador == 1:
         if golpe == True:
            tabla1[filas][columnas] = " 0 "
         else:
            tabla1[filas][columnas] = " x "
      elif jugador == 2:
         if golpe == True:
            tabla2[filas][columnas] = " 0 "
         else:
            tabla2[filas][columnas] = " x "
      print("\t\t\t\t\t\tTABLERO DE BATALLA NAVAL\t\t\t")
      fila ="   1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20"
      for a in range(20):
         if a == 0: 
            print(fila, fila, sep = "\t\t|\t")
         print(a+1, end = " ")
         for b in range(20):
            print(tabla1[a][b], end = "")
         print("\t\t|\t", a+1,  end = " ")
         for c in range(20):
            print(tabla2[a][c], end = "")   
         print()
      print("\n")
   except Exception as e:
      print(e)
   return tabla1, tabla2

def date_error(fila, columna, orientacion="v"):
   ori = ("v","h")
   try:
      if not fila.isdigit() or not columna.isdigit(): raise ValueError("No pude convertir los datos a un entero")
      fila, columna = int(fila), int(columna)     
      if ((fila not in range(1,21) or columna not in range(1,21))): raise IndexError("Ubicacion Invalida, intenta nuevamente")
      if orientacion.lower() not in ori: raise ValueError("Orientacion Incorrecta !!!")
      return True   
   except IndexError as e:
      print(e)
   except ValueError as z:
      print(z)
   except Exception as e:
      print("excepcion rara: ", e)
   return False

def posicion_disparo():
   while True:
      try:
         fila, columna = input("Ingrese la posicion a la que desea disparar, EJ( 7-3 )"+"\t: ").strip().split("-")
         if date_error(fila, columna):       
            return {"posicion": fila+columna,"fila": int(fila), "columna": int(columna)}
         continue
      except ValueError:
         print("No pude convertir los datos a un entero")
      except Exception as e:
         print("¡¡ ERROR !!, Ingresa los datos nuevamente") # terminar de organizar enseguida


def iniciar_juego():
   datos = {"tabla": llenar_tablas(),
            "barcos":{"acorazado":[], "destructor": [], "patrullero": []},
            "NumeroBarcos": 3}


   DatosJuego = {1: datos,
                 2: copia(datos),
                 "campo": {1:llenar_tablas(),2:llenar_tablas()}
                 }
   for jugador in range(1,3):
      print(f"\t\t\t\tJugador {jugador} ingresa tus barcos\n")
      DatosJuego[jugador] = llenar_posiciones(DatosJuego[jugador])
   tablero(DatosJuego[1]["tabla"], DatosJuego[2]["tabla"])
   print(DatosJuego[1]["barcos"])
   print(DatosJuego[2]["barcos"])
   var = True
   while var == True:  # Empiezan los disparos
      for jugador in range(2,0,-1):
         CampoInverso = {1: 2, 2: 1}
         print(f"\t\t\tJugador {CampoInverso[jugador]} Dispara al enemigo...")
         DatosJuego= disparar(DatosJuego,jugador, posicion_disparo(), CampoInverso[jugador])
         if DatosJuego[jugador]["NumeroBarcos"] == 0:
            print(f"Jugador {CampoInverso[jugador]} has ganado la batalla .-------------------.")
            var = False
            break
   print("Fin del juego.... Vuelve pronto")

        
iniciar_juego()

# fin del juego, luego face de modificaciones
# 21-05-36 MODIFICACIONES en try except
# finalizacion proyecto 06-06-2021, implementar proximos array numpy y pandas dataframe
# luego una interfaz grafica mejor, implementar si al ingresar un barco este se encuentra encima de otro
