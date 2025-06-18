#un programa que cuente cuantas vocales hay en una palabra o frase
pal_fras = str(input("ingrese una palabra o una frase:"))
cont = 0
for i in pal_fras:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        cont+=1

print ("en la palabra/frase",pal_fras, "hay ",cont ,"vocales")
