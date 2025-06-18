import math as mt
frutas = {'platano':1.35, 'manzana':0.80, 'pera':0.85, 'naranja':0.70}

eleccion = str(input(f"elija una de las opciones de frutas: {frutas}:"))

while eleccion not in frutas:
    print("la fruta seleccionada no esta dentro del catalogo, ingrese otra")
    eleccion = str(input(f"elija una de las opciones de frutas: {frutas}:"))
else:
    kilos = float(input("ingrese la cantidad en kilos de la fruta seleccionada:"))
    total = frutas[eleccion] * kilos
    print (f"el total seria de {mt.floor(total)}")
