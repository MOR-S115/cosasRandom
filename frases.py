palabras = {}
def deFraseAPalabras(frase):
    porPartes = frase.split()
    for palabra in porPartes:
        palabras[palabra] = len(palabra), "letras"
    print(palabras)


frase = str(input("ingrese una frase cualquiera:"))

deFraseAPalabras(frase)



