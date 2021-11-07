
while True: # para cuestioens de comprobacion
    
    datos = tuple(map(int, input().split()))# entrada de datos casteada a enteros
    ancho1 = datos[0]
    alto1 = datos[1]
    ancho2 = datos[2]
    alto2  = datos[3]

    areaRoja =((ancho1+2)*(alto1+1))-(ancho1*alto1) # area de abajo, se forma un rectangulo y s ele resta lo que tiene
    areaAzul =((ancho2+2)*(alto2+1))-(ancho2*alto2)
    areatotal = areaAzul + areaRoja
    if ancho2 < ancho1:
        extra = ancho1 - ancho2
        areatotal += extra
    print(areatotal)


    

