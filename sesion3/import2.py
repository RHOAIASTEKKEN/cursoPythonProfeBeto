import urllib.request

url = 'https://es.wikipedia.org/wiki/Wikipedia:Portada'

# Realiza la solicitud
dataWeb = urllib.request.urlopen(url)

# Lee el contenido de la respuesta
content = dataWeb.read()

# Guarda el contenido en un archivo
with open('import2.txt', 'wb') as archivo:
    archivo.write(content)

print(f'El contenido ha sido guardado en "import2.txt"')

print("selecicon de datos compartido de la seleccion de los demas componentes ")