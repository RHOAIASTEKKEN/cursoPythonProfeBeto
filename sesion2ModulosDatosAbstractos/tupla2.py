manejoColores = ("ROSA","VERDE","AZUL","ROJO","NEGRO", 1.8,2.5,3.2,1,2,3,4,5)

print("forma simple",manejoColores)

for color in manejoColores:
    print("valor de tupla: ",color)
    
print("\n\nsolo una tupla", manejoColores[5])
print("\n\nvarias una tupla", manejoColores[5:7])


nombreProductos = ("TV","Tablet","radio")
precioProductos = ("TV","Tablet","radio")

totalGeneralTuplas = manejoColores, nombreProductos, precioProductos
print(totalGeneralTuplas)