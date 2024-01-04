# mini program

def datos():
    num1 = float(input("captura numero 1\n"))
    num2 = float(input("captura numero 2\n"))
    return num1, num2

def suma():
    num1, num2 = datos()
    suma = num1 + num2
    print("suma es: ", suma)
    
    
def resta():
    num1, num2 = datos()
    resta = num1 - num2
    print("resta es: ", resta)
    
def multiplicacion():
    num1, num2 = datos()
    multiplicacion = num1 - num2
    print("multiplicacion es: ", multiplicacion)
    
def division():
    num1, num2 = datos()
    division = num1 - num2
    print("division es: ", division)
    
opcion = int(input("selecciona una opcion\n 1.- suma\n 2.- resta\n 3.- multiplicacion\n 4.- division\n"))


for i in range(4):
    if(opcion == 1):
        suma()
    elif(opcion == 2):
        resta()
    elif(opcion == 3):
        multiplicacion()
    elif(opcion == 4):
        division()
        
    else:
        print("la opcion no existe")