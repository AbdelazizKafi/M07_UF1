# Importo les  funcions del fitxer per poder accedir a la bbdd.
from conn import conn, connection

# Aquesta serà la funció que mostrarà els jugadors de la taula a la terminal.
# Només cal fer un SELECT de tots els registres de la taula JUGADORS.
# La funció fetchall mostra els resultats en una llista de tuples.
def llegir_jugadors():
    try:
        sql = "SELECT * FROM JUGADORS"
        connection.execute(sql)
        jugadors = connection.fetchall()

        for jugador in jugadors:
            print(jugador)

    except Exception as error:
        print("Error al llegir els jugadors:", error)
