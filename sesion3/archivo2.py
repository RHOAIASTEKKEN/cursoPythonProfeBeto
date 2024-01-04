import os
import sys

dirActual = os.getcwd()

print("path es: ", dirActual)

passwords = set()

try:
    # Abre el archivo 'archivo.txt' en modo lectura
    with open('archivo.txt', 'r') as fichero:
        for line in fichero:
            passwords.add(line.strip())
except FileNotFoundError:
    print("El archivo no se encuentra.")
    sys.exit()

password_ingresado = input("Ingresa el password a buscar\n")

if password_ingresado in passwords:
    print("Password encontrado y es:", password_ingresado)
else:
    print("No se encontró el password:", password_ingresado)
