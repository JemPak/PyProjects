
datos = tuple(map(int, input().split()))

MCD = 0

for i in range(1,min(datos)):
    var = True
    for j in datos:
        if not j % i == 0:
            var = False
            break
    if var == True:
        MCD = i

print("Maximo comun divisor", MCD)


finish = True
MCM = []
n=2
while finish:
    for i in range(n,min(datos)):
        comprobar = list(filter(lambda x: x%i==0, datos)) 
        if not any(comprobar):continue
        lista = list(map(lambda x: x//i if (x%i==0) else x, datos))
        comprobar2 = list(filter(lambda x: x==1, lista)) 
        if all(comprobar):
            finish = False
            break  
        else:
            n=2
            break          
print(MCM)
