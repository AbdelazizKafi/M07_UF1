# Creo el diccionari amb les divises que desitjo
divises = {
    "Euro": "€",
    "Dòlar": "$",
    "Iene": "¥",
    "Lliura esterlina": "£",
    "Franc suís": "CHF",
    "Dòlar canadenc": "C$",
    "Dòlar australià": "A$",
    "Rupia índia": "₹",
    "Rublo rus": "₽",
    "Yuan xin": "¥"
}

# Demanao a l'usuari que introdueixi una divisa
divisa_input = input("Introdueix el nom d'una divisa: ")

# Comprovo si la divisa està al diccionari i mostro el seu símbol (la divisa s'ha d'escriure amb la seva majuscula ja que sinó no ho detecta i salta l'error)
if divisa_input in divises:
    print(f"El símbol de la {divisa_input} és: {divises[divisa_input]}")
else:
    print("La divisa que has introduït no està al diccionari.")
