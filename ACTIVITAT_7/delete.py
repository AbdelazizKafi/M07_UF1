# Importo les  funcions del fitxer per poder accedir a la bbdd.
from conn import conn, connection

# Aquesta funcio es una mica semblant a l'anterior.
# L'usuari tindrà que seleccionar l'abreviació del jugador que desitja eliminar.
def eliminar_jugador(abreviacio):
    sql = "DELETE FROM JUGADORS WHERE abreviacio = %s"
    try:
        connection.execute(sql, (abreviacio,))
        conn.commit()
        print("Jugador eliminat correctamente.")
    except Exception as error:
        print("Error al eliminar el jugador:", error)
# Aquí si que podria tancar les connexions a la bbdd ja que es la ultima funció de l'ultim fitxer.
# Si dona errors es podria eliminar aquesta ultima part, pero funciona correctament.
    finally:
        connection.close()
        conn.close()