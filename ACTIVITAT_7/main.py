# Importo les funcions del fitxer conn i també les funcions dels fitxers CRUD.
from conn import conn, connection
from create import crear_jugador
from read import llegir_jugadors
from update import actualitzar_jugador
from delete import eliminar_jugador

# Creo el menú principal en el qual l'usuari utilitzarà per seleccionar el que vol fer.
def mostrar_menu():
    print("\nMenú d'opcions CRUD:")
    print("1. Crear un nou jugador")
    print("2. Llegir jugadors")
    print("3. Actualitzar un jugador")
    print("4. Eliminar un jugador")
    print("5. Sortir")

# Funció que permet a l'usuari seleccionar l'opció que vol fer.
# Quan acabi una funció, es torna a mostrar el menú principal.
def main():
    while True:
        try:
            mostrar_menu()
            opcion = input("Selecciona una opción del 1 al 5: ")

            # Si l'usuari selecciona la opció 1, es crida la funció crear_jugador.
            # L'usuari té que introduïr els valors que es demanen per crear el jugador.
            if opcion == "1":
                abreviacio = input("Abreviació del jugador: ")
                nom = input("Nom del jugador: ")
                equip = input("Equip del jugador: ")
                posicio = input("Posició del jugador: ")
                gols = int(input("Gols del jugador: "))
                trofeus = int(input("Trofeus del jugador: "))
                crear_jugador(abreviacio, nom, equip, posicio, gols, trofeus)

            # Si l'usuari selecciona la opció 2, es crida la funció llegir.
            # S'imprimeix per terminal tots els jugadors que hi ha en la base de dades.
            elif opcion == "2":
                llegir_jugadors()

            # Si l'usuari selecciona la opció 3, es crida la funció actualitzar_jugador.
            # L'usuari té que introduïr l'abreviació del jugador que vol actualitzar i seguidament les seves noves dades.
            elif opcion == "3":
                abreviacio = input("Abreviació del jugador a actualizar: ")
                nom = input("Nou nom del jugador: ")
                equip = input("Nou equip del jugador: ")
                posicio = input("Nova posició del jugador: ")
                gols = int(input("Nous gols del jugador: "))
                trofeus = int(input("Nous trofeus del jugador: "))
                actualitzar_jugador(abreviacio, nom, equip, posicio, gols, trofeus)

            # Si l'usuari selecciona la opció 4, es crida la funció eliminar_jugador.
            # L'usuari té que introduïr l'abreviació del jugador que vol eliminar.
            elif opcion == "4":
                abreviacio = input("Abreviació del jugador a eliminar: ")
                eliminar_jugador(abreviacio)

            # Si l'usuari selecciona la opció 5, es surt del programa.
            elif opcion == "5":
                print("Saliendo del programa...")
                break

            # Si l'usuari selecciona un número o valor que no sigui del 1 al 5, es mostra un missatge d'error.
            else:
                print("Opción no válida. Intente de nuevo.")
        
        except ValueError as e:
            # Faig aquest except en cas de que l'usuari introdueixi un valor no vàlid
            print(f"Error de valor: {e}. Asegúrese de ingresar un número válido.")
        
        except Exception as e:
            # Capturo qualsevl altre error
            print(f"Ocurrió un error: {e}")
        
        finally:
            # Tanco la connexió i el cursor després que totes les operacions hagin acabat
            if conn and connection:
                connection.close()
                conn.close()
                print("Connexió a la base de dades tancada correctament.")

if __name__ == "__main__":
    main()
