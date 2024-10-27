# Creo la llista amb les 6 assignatures
asignatures = ["Matemàtiques", "Llengua", "Història", "Ciències", "Educació Física", "Anglès"]

# Inicialitzo una llista per introduir les notes i guardarles
notes = []

# Demano a l'usuari que introdueixi les notes de les 6 matèries que poden ser amb numeros decimals
for assignatura in asignatures:
    nota = float(input(f"Introdueix la nota per {assignatura}: "))
# Emmagatzemo les notes a la llista creada previament
    notes.append(nota)

# Mostro les notes amb el seu text
for i in range(len(asignatures)):
    print(f"A {asignatures[i]} ha tret {notes[i]:.2f}.")
