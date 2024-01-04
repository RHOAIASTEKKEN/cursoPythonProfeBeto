import modulos

a = float(input("1er numero\n"))
b = float(input("2do numero\n"))

rSuma = modulos.sumar(a,b)
rResta = modulos.resta(a,b)
rMultiplicacion = modulos.multiplicacion(a,b)
rDivision = modulos.division(a,b)

print("suma es -->",rSuma, "\n",
      "resta es -->",rResta, "\n",
      "multiplicacion es -->",rMultiplicacion, "\n",
      "division es -->",rDivision, "\n",)


print("Area del circulo es: ", modulos.pi*2*2)