import os
import time as tm

ancho = 20

for i in range(ancho + 1):
    porcentaje = int(i / ancho * 100)
    os.system("cls")
    barra = "#" * i + "-" * (ancho - i)
    print (f"{barra} {porcentaje}%")
    tm.sleep(0.1)