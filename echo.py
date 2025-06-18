#se creo la lista echo
echo=[]
#se inicializa la variable entrada 
entrada=""
#se crea un bucle while con la variable entrada y el string de salir
while entrada != "salir":
    entrada=input("escribe cualquier cosa :v, para terminar escribe salir:")
    #se pregunta si en la variable entrada existe el string salir, si no es asi, la extencion .append agrega el valor de entrada a la lista echo
    if entrada != "salir":
        echo.append(entrada)
#el bucle for imprime en pantalla los valores de la lista 
for i in echo:
    print(i)


    
    