import calendar


yy=2024
mm=1
print("Fecha es: ", calendar.month(yy,mm))

def anagram(wordl, wordl2):
    wordl = wordl.lower()
    wordl2 = wordl2.lower()
    return sorted(wordl) == sorted(wordl2)

print("resultado de la comparacion \n", anagram("cinema", "iceman"))
print("resultado de la comparacion \n", anagram("cool", "loco"))
print("resultado de la comparacion \n", anagram("men", "woman"))