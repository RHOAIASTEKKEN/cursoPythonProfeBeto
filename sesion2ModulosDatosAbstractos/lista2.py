listNames = ["Pablo", "Ana", "Joel", "Kevin"]

indiceBusqueda = int(input("numero de indice a buscar\n"))

if indiceBusqueda<len(listNames):
    print(listNames[indiceBusqueda])
    
else:
    print("no se encontro")