import random

print("Generator password charater requerid\n")

passlen = int(input("Cuantos digitos va a tener el password \n"))
bancoSimbolos = "qwertyuiopñlkjhgfdsazcvbnm0123456789°!#$%&/()=?¡*¨[]{-}_.,"

p = "".join(random.sample(bancoSimbolos, passlen))

print("El password generado es -->",p)