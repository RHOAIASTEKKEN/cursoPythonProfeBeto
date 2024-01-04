while True:
        print("MENU INVENTARIOS\n",
        "1.- Ingresar Producto\n",
        "2.- Consultar producto\n",
        "3.- Comprar producto\n",
        "4.- SALIR\n",)
        opc = int(input("que opcion quieres consultar"))


        if(opc == 1):
            print("Ingresar Producto\n")
            
        elif(opc == 2):
            print("Consultar producto\n")
            
        elif(opc == 3):
            print("Comprar producto\n")
            
            
        elif(opc == 4):
            print("salir\n")
            break
            
            

        else:
            print("\n\033[91mSELECCIONA UNA OPCION VALIDA\033[0m", "\n\n")