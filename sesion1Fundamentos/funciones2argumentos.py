
def area(lado):
    return lado*lado

def perimetro(lado):
    return 4 * lado


try:
    lado = float(input("cual es el valor del lado\n\n"))
    if(lado<=0):
        print("\033[91merror de sistema, ingresa medidad valida, MAYOR A CERO 0\033[91m \n\n")
    else:
        areaC= area(lado)
        perimetroC = perimetro(lado)
        print("el area es: ",areaC, "\n el perimetro es: ", perimetroC)
    
except ValueError:
    print("\033[91merror de sistema, ingresa medidad valida\033[91m \n\n")