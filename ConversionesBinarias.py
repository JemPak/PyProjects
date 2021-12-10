"""
   author   @Juan Jose Monsalve
   14/10/2021

   Descripción: Script para hacer conversiones entre los sistemas
   de unidades decimales, babilonios y binarios.
   
"""


from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

v = Tk()
v.wm_title("Sistema de Conversión")
v.minsize(width=280, height=200)

Label(v, text="Conversión de:").grid(row=0, column=0)
Label(v, text="A:").grid(row=2, column=0)

denominaciones = ["Número Decimal", "Número Babilonio", "Número binario"]

entrada=Combobox(v)
entrada["values"]=denominaciones
entrada.grid(row=0, column=1)

salida=Combobox(v)
salida["values"]=denominaciones
salida.grid(row=2, column=1)

value = Entry(v, width=30)
value.grid(row=1, column=1)

text = "Para números decimales utilice y<\nluego separe con espacio\nEJM:  <<<y <<y y = 112861"
mesage = Text(v, width=35, height=5)
mesage.insert(INSERT, text)
mesage.configure(state=DISABLED)
mesage.place(x=10, y=100)

def BabilonioaDecimal(nums: list) -> int:
   ''' Esta funcion convierte un numero babilonio a un numero árabigo
      Ejm:
         lista = [ "<<<y", "yy<", "<<"]
      se recorre la lista y la suma de cada elemento se multiplica por 60 a la n.
   '''
   base = 60
   respuesta = 0
   for index, value in enumerate(nums):
      diez = value.count("<")
      uno = value.count("y")
      respuesta += ((diez*10)+uno)*(60**index)
   return respuesta

def DecimalAbinario(num):
   """funcion que convierte un numero decimal a binario"""
   binary = 0
   result = ""
   long = len(str(num))
   while True:     
      if 2**binary > num:
         binary -= 1
         break
      else:
         binary += 1
   while binary != -1 or num!=0:
      if num >= 2**binary:
         num -= (2**binary)
         result += "1"
      else:
         result += "0"
      binary -= 1
   dif = long-len(result)
   result += "0"*dif
   return result

def BinarioaDecimal(numero: str) -> int:
   """funcion que convierte un binario en numero decimal"""
   result = 0
   for i in range(len(numero)):
      if numero[i] == "1":
         result += 2**i
   return result

def sobras(num):
   decena = "<"
   unidad = "y"
   U_d = num//10
   U_u = num-U_d*10
   cadena = decena*U_d + unidad*U_u
   return cadena

def DecimalAbabilonio(num):
   """funcion que convierte un decimal en numero babilonio"""
   result = []
   index = 0
   conter = 0
   while True:      
      if 60**index > num:
         index -= 1
         break
      else:
         index += 1
   while index!=-1:
      middle = 60**index
      cont = 0
      while middle*cont <= num:
         cont += 1
      middle *= cont-1
      num -= middle
      result += [sobras(cont-1)]
      index -= 1
   return result  
      
         
def convertir():
   sistema_ent = entrada.current()
   sistema_sal = salida.current()
   respuesta = ""
   num = str(value.get())
   if sistema_ent == 0:             # de decimal a
      
      if sistema_sal==1:            # babilonio         
         respuesta = DecimalAbabilonio(int(num))
         respuesta = "  ".join(respuesta)
      elif sistema_sal==2:          # binario
         respuesta = DecimalAbinario(int(num))
      else:                                  #error
         messagebox.showerror("", "datos no válidos")

         
   elif sistema_ent == 1: # de babilonio a:
      if sistema_sal==0:# decimal
         nums = num.split()[::-1]
         respuesta = BabilonioaDecimal(nums)
      elif sistema_sal==2:#binario
         nums = num.split()[::-1]
         respuesta = BabilonioaDecimal(nums)
         respuesta = DecimalAbinario(respuesta)
      else:                         #error
         messagebox.showerror("", "datos no válidos")
         
    
   else: # de binario a:      
      if sistema_sal==0:# decimal
         respuesta = BinarioaDecimal(num[::-1])         
      elif sistema_sal==1:# babilonio
         num = BinarioaDecimal(num[::-1])
         respuesta = DecimalAbabilonio(num)
      else:
         #error
         messagebox.showerror("", "datos no válidos")
      
   mesage.configure(state=NORMAL)
   mesage.delete("1.0", "end")
   mesage.insert(INSERT, respuesta)
   mesage.configure(state=DISABLED)
         

Button(v, text="Realizar Conversión", command=convertir).grid(row=3, column=0)
