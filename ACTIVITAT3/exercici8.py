# Demano a l'usuari que introdueixi 10 números separats per espais
entrada = input("Introduce 10 números separados por espacios: ")

# Utilitzo aquesta funcio per separar els 10 numeros
numeros = entrada.split()
# Converteixo la cadena introduida en una llista d'enters
numeros = [int(num) for num in numeros]

# Faig el calcul de la suma i la mitjana
suma_total = sum(numeros)
mitjana = suma_total / len(numeros)

# Afeigeixo aquestes dues variables a la llista
numeros.append(suma_total)
numeros.append(mitjana)

# Imprimeixo els resultats
print("\nNúmeros de l’usuari:", numeros[:-2])
print("Suma total:", suma_total)
print("Mitjana:", mitjana)
print("Llista completa amb suma i mitjana:", numeros)
