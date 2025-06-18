frase=input("ingrese una frase a su preferencia:")
letra=input("ingrese la letra que desea ver que mas se repite:")
cont=0
for i in frase:
    if i==letra:
        cont+=1
print("la letra",letra,"se repitio un total de",cont,"en la frase",frase)
    