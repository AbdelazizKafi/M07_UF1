
preu = int(input("Introdueix el valor en euros: "))
iva = 0

while iva not in [4, 10, 21]:
    iva = int(input("Introdueix l'IVA (4, 10 o 21): "))

preu_final = preu + preu * iva / 100

print("Preu original:", preu, "€")
print("Percentatge d'IVA:", iva, "%")
print("Preu final amb IVA:", preu_final, "€")
