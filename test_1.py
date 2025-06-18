
def cal():
    costo=float(input("ingrese el precio del producto:"))
    iva_p=input("ingrese el porsentaje de iva a aplicar:")

    if iva_p.strip()=="":
        iva=21
    else:
        iva=float(iva_p)

    resultado=costo*(1+iva/100)    
    print("el precio con el iva de ",iva,"%"," es de:",resultado)
cal()