import os

#para ejecutar una instruccion o comando msdos (sistema oeprativo)
cmd="netsh wlan show profile"
resultado=os.popen(cmd)
print(resultado.read())

#Crea archivo tipo excel universal y lo abre para escritura
mi_archivo=open('redeswi.csv','a')
red=str(input("Ingrese el nombre o NICKMANE de la red :"))

#genera escaneo de redes con password
cmd2="netsh wlan show profile"+red+" key=clear"
resultado2=os.popen(cmd2)

#grabar los datos en el archivo excel universal redeswi.csv
mi_archivo.write(resultado2.read())