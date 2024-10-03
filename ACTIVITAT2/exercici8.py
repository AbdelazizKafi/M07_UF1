input_paraules = input("Introdueix entre 1 i 3 paraules, separades per espais: ")

paraules = divisio.split()

if 1 <= len(paraules) <= 3:
    for paraula in paraules:
        print("Paraula:", paraula)
        print("Nombre de caràcters:", len(paraula))
        print("Primer caràcter:", paraula[0])
        print("Últim caràcter:", paraula[-1])
        print()  
else:
    print("Error: Has d'introduir entre 1 i 3 paraules.")
