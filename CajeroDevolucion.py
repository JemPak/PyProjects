#Importar la libreria para GUI
from tkinter import * 
from tkinter import messagebox

import re

ventana = Tk()
ventana.wm_title("Devolución Dinero")
ventana.minsize(width=600, height=250)

denoms = [50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50]
txtDevuelta = Entry(ventana, width=15)
txtDevuelta.grid(row=0, column=1)
Label(ventana, text="Devolver").grid(row=0, column=0)
Label(ventana, text="Denominación").grid(row=1, column=0)
Label(ventana, text="Existencia").grid(row=1, column=1)
Label(ventana, text="Devuelta").grid(row=1, column=2)

Denominacion=[]
Existencia = []
devuelta = []
for i in range(10):
   for j in range(3):
      if j == 0: # denominacion
         caja = Entry(ventana, width=15)
         caja.grid(row=i+2, column=j)
         caja.insert(0,str(denoms[i]))
         Denominacion.append(caja)
      elif j == 1: # existencia
         caja = Entry(ventana, width=15)
         caja.grid(row=i+2, column=j)
         caja.insert(0, "0")
         Existencia.append(caja)
      else: # devolucion
         caja = Entry(ventana, width=15)
         caja.grid(row=i+2, column=j)
         caja.insert(0, "0")
         caja.configure(state=DISABLED)
         devuelta.append(caja)
mesage = Text(ventana, width=35, height=12)
mesage.configure(state=DISABLED)
mesage.place(x=300, y=50)

# Funcion para actualizar los valores a devolver
# La misma funcion actualiza los campos de existencias disminuyendo lo devuelto
def Operacion_Cajero(A_devolver):
   FinalMesage = "La devuelta se compone de:\n" # formacion del mensaje final a imprimer en el Text
   CleanDevuelta()
   copia = CopyValues() # copia de los valores en existencia por si la solucion no es exacta
   index = 0
   while A_devolver != 0 and index !=10: # hasta devolver completamente o por si la cifra no es exacta
      denominado = int(Denominacion[index].get())
      existen = int(Existencia[index].get())
      if existen > 0 :
         cantidad = A_devolver // denominado
         if cantidad > 0:
            if cantidad > existen:
               cantidad = existen
            A_devolver -= cantidad*denominado
            devuelta[index].configure(state=NORMAL)
            devuelta[index].delete(0, END)
            devuelta[index].insert(0, str(cantidad))
            devuelta[index].configure(state=DISABLED)
            Existencia[index].delete(0, END)
            Existencia[index].insert(0, str(existen-cantidad))
            if len(Denominacion[index].get()) >= 4:
               FinalMesage += f"{cantidad} billete de $ {float(denominado):,.0f}\n"
            else:
               FinalMesage += f"{cantidad} moneda de $ {float(denominado):,.0f}\n"
      index += 1
   #print(FinalMesage)
   if A_devolver == 0:
      mesage.configure(state=NORMAL)
      mesage.delete("1.0", "end")
      mesage.insert(INSERT, FinalMesage)
      mesage.configure(state=DISABLED)
   else:
      RestaureValues(copia) # restaurar los valores en existencia por si al devuelta no está completa
      mesage.configure(state=NORMAL)
      mesage.delete("1.0", "end")
      mesage.insert(INSERT, "No contamos con la \ndevuelta completa")
      mesage.configure(state=DISABLED)


def CleanDevuelta():
   for i in range(10):
      devuelta[i].configure(state=NORMAL)
      devuelta[i].delete(0, END)
      devuelta[i].insert(0, "0")
      devuelta[i].configure(state=DISABLED)
# Copia de los valores en existencia
def CopyValues():
   copia = []
   for i in range(10):
      copia.append(Existencia[i].get())
   return copia

# restaurar los valores de existencia anteriores
def RestaureValues(valores):
      for i in range(10):
         Existencia[i].delete(0, END)
         Existencia[i].insert(0, valores[i])
                        
def evaluarDevuelta():
   var = True
   for i in range(10): # revisamos que las denominanciones y existencias esten completas
      if re.match("^[0-9]+[.]?[0-9]*$", Denominacion[i].get()) and \
        re.match("^[0-9]+[.]?[0-9]*$", Existencia[i].get()) and re.match("^[0-9]+[.]?[0-9]*$", txtDevuelta.get()):
         continue
      else: # nos aseguramos de que los datos  esten completos
         var = False
         break
   if var == False:
      messagebox.showerror("", "Ingresa todos lo datos completos")
   else: 
      Operacion_Cajero(int(txtDevuelta.get()))        # valor al cual se debe devolver
   
Button(ventana, text="Devolver", command=evaluarDevuelta).grid(row=0, column=0)
   
