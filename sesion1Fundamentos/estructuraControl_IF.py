user = str(input("Nombre del usuario\n"))
password = str(input("\n\npassword del usuario\n"))

if(user == "tony" and password == "tony"):
    cal1=float(input("calificacion 1\n"))
    cal2=float(input("calificacion 2\n"))
    cal3=float(input("calificacion 3\n"))

    promedio = (cal1 + cal2 +cal3) / 3

    if (promedio >= 6):
        print("\n\nAprobado \n",
              "boleta de calificaciones \n",
              "calificacion 1 -->", cal1,
              "\ncalificacion 2 -->", cal2,
              "\ncalificacion 3 -->", cal3,
              "\npromedio es--> ", promedio,)
    else:
        print("\n\nNO Aprobado \n",
            "boleta de calificaciones \n",
            "\ncalificacion 1 ", cal1,
            "\ncalificacion 2 ", cal2,
            "\ncalificacion 3 ", cal3,
            "\npromedio es--> ", promedio,)
else:
    print("\nEl usuario no existe\n")