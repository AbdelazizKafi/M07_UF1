# Funció per calcular el preu final amb IVA
def calcular_preu_amb_iva(preu, iva):
    iva_decimal = iva / 100  # Convertir l'IVA a decimal
    preu_final = preu * (1 + iva_decimal)
    return preu_final

# Demanar el valor en euros
preu = float(input("Introdueix el valor en €: "))

# Demanar el percentatge d'IVA fins que sigui correcte
while True:
    iva = int(input("Introdueix el percentatge d'IVA (4, 10, 21): "))
    if iva in [4, 10, 21]:
        break  # Si és vàlid, sortir del bucle
    else:
        print("IVA no vàlid. Si us plau, introdueix 4%, 10% o 21%.")

# Calcular el preu final
preu_final = calcular_preu_amb_iva(preu, iva)

# Mostrar els resultats
print(f"Valor indicat: {preu} €")
print(f"Percentatge d'IVA: {iva}%")
print(f"Preu final amb IVA: {preu_final:.2f} €")
