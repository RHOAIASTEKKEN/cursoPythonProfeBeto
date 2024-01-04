from countryinfo import CountryInfo

# Lee el nombre del país desde la entrada del usuario
country_name = str(input("Nombre del país para analizar datos: "))

# Crea un objeto CountryInfo para el país especificado
country_info = CountryInfo(country_name)

# Accede a los datos del país utilizando los métodos proporcionados por CountryInfo
print("Capital: ", country_info.capital())
print("Monedas: ", country_info.currencies())
print("Idiomas: ", country_info.languages())
print("Fronteras: ", country_info.borders())
print("Other Name: ", country_info.alt_spellings())
