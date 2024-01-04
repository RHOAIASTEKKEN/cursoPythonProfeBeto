import hashlib

passwordEncriptar = str(input("captura el password"))

print("--------------------------MSD")

h=hashlib.md5()
h.update(passwordEncriptar.encode('utf-8'))
print(h.hexdigest())