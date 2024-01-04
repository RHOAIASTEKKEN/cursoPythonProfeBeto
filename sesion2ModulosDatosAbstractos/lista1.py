frutas = ["naranja","manzanas","pera","banana","kiwi","manzanas","banana"]

print("elementos frutas ", frutas)


for i in frutas:
    print("fruta almacenada", i)
    
print("numero de manzanas es", frutas.count("manzanas"))
print("numero de banana es", frutas.count("banana"))
print("numero de naranja es", frutas.count("naranja"))
print("pera esta en la posicion", frutas.index("pera"))
print("agregar fruta ", frutas.append("uva"))
print("agregar fruta ", frutas.append("nuez"))
    
for position1 in frutas:
    print("fruta almacenada", position1)
    break