# Creo la llista amb les lletres de l'abecedari
abecedari = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z"
]

# Mostro la llista original amb les lletres del abecedari
print("Llista original:", abecedari)

# Elimino les lletres en posicions múltiples de 3 amb aquesta funció
abecedari = [letra for i, letra in enumerate(abecedari) if (i + 1) % 3 != 0]

# Converteixo la llista resultant en una tupla
tupla_resultant = tuple(abecedari)

# Mostro la llista original i la tupla
print("Tupla :", abecedari)
