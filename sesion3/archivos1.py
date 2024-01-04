import os

dirActual = os.getcwd()
listActual = os.listdir(dirActual)
numeroAlumnos = 0


print("la path es: ", dirActual)
print("la path es: ", listActual)

f=open('notas.txt', 'wt')


numeroAlumnos = int(input("\ncontrol ESCOLAR\n CUANTOS ALUMNOS DESEAS AGREGAR\n"))

for _ in range(numeroAlumnos):
    matricula = int(input("\ncaptura 4 numeros para matricula\n"))
    cal1 = float(input("captura 1er calificacion\n"))
    cal2 = float(input("captura 2da calificacion\n"))
    cal3 = float(input("captura 3er calificacion\n"))
    
    prom = (cal1+cal2+cal3)/3
    
    f.write(f"Matrícula: {matricula}, Promedio: {prom}\n")
f.close