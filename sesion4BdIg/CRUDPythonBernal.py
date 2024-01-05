import mysql.connector
from colorama import Fore, Style

conexion = mysql.connector.connect(host="localhost",
                                  user="root",
                                  passwd="",
                                  database="bdPythonBernal")

cursor = conexion.cursor()

# Obtener la lista de tablas
cursor.execute("SHOW TABLES")


tablas = cursor.fetchall()

cursor.execute("SELECT VERSION()")
version = cursor.fetchone()
print(f"Versión de MySQL: {version[0]}")

while True:
    # Recorrer las tablas
    for (tabla,) in tablas:
        print(f"{Fore.BLUE}\nContenido de la tabla {tabla}:\n{Style.RESET_ALL}")

        # Obtener todas las columnas de la tabla
        cursor.execute(f"SELECT * FROM {tabla}")
        
        # Obtener los nombres de las columnas
        columnas = [column[0] for column in cursor.description]
        print("\t".join(columnas))

        # Mostrar los datos
        for fila in cursor:
            print("\t".join(str(valor) for valor in fila))
            
        print(f"{Fore.GREEN}\n\n----------------------------MENU -----------------------------------{Style.RESET_ALL}")
        opc = int(input(f"{Fore.GREEN}1.- Agregar registro Nuevo\n2.-Borrar 1 registro\n3.-Actualizar productos\n0.- salir\n{Style.RESET_ALL}"))
        
        if (opc == 1):
            producto = str(input("Nombre del producto:\n"))
            descripcion = str(input("Descripción del producto:\n"))
            cantidad = int(input("Cantidad del producto:\n"))
            precio = float(input("Precio del producto:\n"))
            
            sql = "INSERT INTO productos (nombre, descripcion, cantidad, precio) VALUES (%s, %s, %s, %s)"
            datos = (producto, descripcion, cantidad, precio)
            
            cursor.execute(sql, datos) 
            conexion.commit() #envio de datos
            
            if (conexion.commit()):
                print("Registro agregado exitosamente.", datos)
            else:
                print(f"{Fore.RED}idProducto no borrado correctamente.{Style.RESET_ALL}")
                
        elif(opc == 2):
            print("-------------borrar datos----------------")
            borrar = int(input("coloca idProducto del elemento a borrar"))
            sql = "DELETE FROM productos WHERE idProducto = %s"
            datos =  (borrar,)
            cursor.execute(sql, datos)
            conexion.commit()
            
            if (conexion.commit()):
                print("idProducto borrado correctamente", datos)
            else:
                print(f"{Fore.RED}idProducto no borrado correctamente.{Style.RESET_ALL}")
                
        elif(opc == 3):
            print("-------------Actualizar datos----------------")
            actualizar = int(input("coloca idProducto del elemento a actualizar"))
            
            print("¿Qué deseas actualizar?")
            print("1.- Nombre")
            print("2.- Descripción")
            print("3.- Cantidad")
            print("4.- Precio")
            
            opcion_actualizar = int(input("Selecciona una opción: "))
            
            if opcion_actualizar in (1, 2, 3, 4):
                nuevo_valor = str(input(f"Coloca el nuevo valor para {['nombre', 'descripcion', 'cantidad', 'precio'][opcion_actualizar - 1]}: "))

                # Utiliza parámetros en la consulta para evitar SQL injection
                campos = ['nombre', 'descripcion', 'cantidad', 'precio']
                campo_actualizar = campos[opcion_actualizar - 1]
                sql = f"UPDATE productos SET {campo_actualizar}=%s WHERE idProducto = %s"
                datos = (nuevo_valor, actualizar)

                cursor.execute(sql, datos)
                conexion.commit()

                if cursor.rowcount > 0:
                    print("Registro actualizado correctamente.")
                else:
                    print(f"{Fore.RED}No se encontró un elemento con idProducto {actualizar}.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Opción no válida.{Style.RESET_ALL}")
                
        else:
            print("Terminó la consulta.")
            
            
    repetWhile = int(input(f"{Fore.YELLOW}deseas seguir haciendo cambios\n1.- SEGUIR\n0.-SALIR\n{Style.RESET_ALL}"))
    
    if repetWhile == 1:
        print("")
    else:
        break

cursor.close()
conexion.close()
