#pedir al usuario un numero
num = int(input("ingrese un valor numerico:"))

#usando un condicional if/while se verifica si el valor es menor o igual a 1
while num <= 1:
    num = int(input("valor no valido menor a 1, ingrese otro:"))
#se establece la variable prim como bool=true
prim = True
#usando un bucle se verifica si el modulo de num es igual a cero, si es asi el valor de prim sera false
for i in range(2,num):
    if num % i == 0:
        prim = False
        break
#se compara si prim es true o false
if prim:
    print ("es primo")
else:
    print ("no es primo")

    
        



    