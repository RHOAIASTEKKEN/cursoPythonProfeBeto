import random

dado = random.randint(1, 6)
dado2 = random.randint(1, 6)

suma = dado + dado2

if (suma == 9):
    print("Felicidades ganaste, El numero ganador es: ", suma)
else:
    print("Haz perdido, lanza de nuevo")