##### Solucion por Juan Jose Monsalve #####
#   link:  https://israelem.github.io/aceptaelreto/polidivisibles/ '
def polidivisible(numero):
    ''' paso de parametro un numero como string y evaluo si 
    es polidivisible para agregarlo a la lista global a retornar''' 
    for i in range(1,len(numero)+1):
        if int(numero[:i]) % i != 0:
            break
    else:
        global lista    # llamado a la lista global para agregarlo
        lista += [numero]

def agrandar(N, longitud):
    ''' funcion recursiva que recorre de [0 a 9] agregando el digito.
        vuelvo a llamar la funcion hasta que la longitud sea la minima (1)
        luego por cada numero lo voy mandando a la funcion polidivisible 
        para evaluar si cumple las condiciones'''
    nums = [str(i) for i in range(10)]      # lista de numeros de [0 a 9] 
    if longitud == 1:
        for num in nums:
            numero = N+num
            polidivisible(numero)
    else:
        for num in nums:
            numero = N+num
            polidivisible(numero)
            agrandar(numero, longitud-1)    # recursividad obligada para evaluacion de datos
    
while True:
    entrada = input().split()   # ENTRO NUMERO - RECORRIDO, EJ(2016 5)
    N = entrada[0]
    D =int(entrada[1])
    longitud = D-int(len(N)) # longitud de veces a evaluar
    if longitud == 0:
        print(N)
    else:
        lista = []
        lista += [N]
        agrandar(N, longitud)
        for numeros in lista:
            print(numeros)
    print("---")

### del deivi




def es_polidivisible(num):
    x=len(str(num))
    y=len(str(num))
    espol=False
    cont=0
    while num>0:
        if num%x==0:
            x=x-1
            num=num//10
            cont+=1
        else:
            break
    if cont==y:
        espol=True
    return espol
def lista_e(x):
    lista=[]
    lista2=[]
    ceros="0"
    uno="1"
    nueves="9"
    if x==1:
        for i in range(0,10):
            lista2.append(str(i))
    else:
        r=uno+((x)*ceros)
        h=uno+((x)*nueves)
        for i in range(int(r),int(h)+1):
            lista.append(str(i))
        for e in lista:
            numero=e[1::1]
            lista2.append(numero)    
    return lista2

N=int(input())
for i in range(N):
    numero=str(input()).split()
    n=int(numero[1])-len(numero[0])
    #print(n)
    if n==0:
        print(numero[0])
        print("---")
    else:
        lista1=[]
        lista2=[]
        lista3=[numero[0]]
        for j in range(1,n+1):
            x=lista_e(j)
            for e in x:
                lista1.append(e)
        for a in lista1:
            b=numero[0]+a
            lista2.append(b)
        for c in lista2:
            if es_polidivisible(int(c))==True:
                lista3.append(c)
        #print(lista3)
        for d in lista3:
            print(d)
        print("---")





