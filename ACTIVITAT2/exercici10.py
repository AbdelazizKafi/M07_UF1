import random

numero_secret = random.randint(1, 100)

intents = 0

encertat = False

while not encertat:
    numero_usuari = int(input("Endevina el número (entre 1 i 100): "))
    intents += 1

    if numero_usuari < numero_secret:
        print("El número és inferior.")
    elif numero_usuari > numero_secret:
        print("El número és superior.")
    else:
        print(f"Has encertat el número {numero_secret} en {intents} intents.")
        encertat = True
