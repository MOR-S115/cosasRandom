palabra=input("ingrese una palabra o frase:")
sinEspacios=palabra.replace(" ","")
pal_in=sinEspacios[::-1]

if pal_in==sinEspacios:
    print("la palabra es polindroma")
else:
    print("la palabra no es polindroma")