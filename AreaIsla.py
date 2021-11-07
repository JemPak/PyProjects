import numpy as np
def mar(indices):
    num = 0
    islas = {}
    for i in range(len(indices)):
        for index in np.where(np.array(indices[i])==1):
            if i == 0:
                lista1 = []
                lista2 = indices[i]
                lista3 = indices[i+1]
            elif i == len(indices)-1:
                lista1 = [i-1]
                lista2 = [i]
                lista3 = []
            else:
                lista1 = [i-1]
                lista2 = [i]
                lista3 = [i+1]
            islas, num = lados(islas,[lista1,lista2,lista3],index, num)
            

# def lados(dic, lados, ind, num):
#     try:
#         if (len(lados[0]) and len(lados[2])) != 0:
#             print()
#             # solo mirar esa lida derecha e izq
#         else:
#             if lados[0][ind]== 1:
#             dict[]







