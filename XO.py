#variables globales
f1,c1,f2,c2=0,0,0,0
#crar una funcion para imprimir un tablero de 9x9 
tablero = [["[ ]", "[ ]", "[ ]"],
           ["[ ]", "[ ]", "[ ]"],
           ["[ ]", "[ ]", "[ ]"]]
def tab_l():
    for fila in tablero:
        print("".join(fila))

#crear dos funciones que pidan a los jugadores ingresar la posicion de la X o O dentro del tablero    
def jugador1():
    print("turno del jugador 1")
    f1=int(input("ingrese la fila donde se colocara la X:"))
    c1=int(input("ingrese la columna donde se colocara la X:"))
    return f1,c1
   
def jugador2():
    print("turno del jugador 2")
    f2=int(input("ingrese la fila donde se colocara el O:"))
    c2=int(input("ingrese la columna donde se colocara el O:"))
    return f2,c2

#funcion para saber si alguien gano
def verificar_ganador():
    # Revisar filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] != "[ ]":
            print(f"¡Ganador encontrado en fila! {fila[0]}")
            return True

    # Revisar columnas
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] != "[ ]":
            print(f"¡Ganador encontrado en columna! {tablero[0][col]}")
            return True

    # Revisar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != "[ ]":
        print(f"¡Ganador encontrado en diagonal principal! {tablero[0][0]}")
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != "[ ]":
        print(f"¡Ganador encontrado en diagonal secundaria! {tablero[0][2]}")
        return True

    return False

#esquema del tablero
def esquema():
    print("  0  1  2")
    print("0 ""[] [] []")
    print("1 ""[] [] []")
    print("2 ""[] [] []")

#hora de crear el juego :v
mv=0
while mv<9:
    esquema()
    f1,c1=jugador1()
    tablero[f1][c1]="[X]"
    print(tab_l())
    if verificar_ganador():
        print("jugador 1 gana")
        break
    mv+=1
    if mv<9:
        f2,c2=jugador2()
        tablero[f2][c2]="[O]"
        print(tab_l())
        if verificar_ganador():
            print("jugador 1 gana")
            break
        mv+=1
    else:
        break

    

    

            
    


        


        

        
    






