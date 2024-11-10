# Importo les  funcions del fitxer per poder accedir a la bbdd.
from conn import conn, connection

# Aquesta funció el que fara serà actualitzar els registres d'un jugador.
# L'usuari tindrà que seleccionar l'abreviació del jugador que desitja actualitzar i després introduïr les seves dades noves.
def actualitzar_jugador(abreviacio, nom, equip, posicio, gols, trofeus):
    sql = '''
    UPDATE JUGADORS
    SET nom = %s, equip = %s, posicio = %s, gols = %s, trofeus = %s
    WHERE abreviacio = %s
    '''
    try:
        connection.execute(sql, (nom, equip, posicio, gols, trofeus, abreviacio))
        conn.commit()
        print("Jugador actualitzat correctament.")
    except Exception as error:
        print("Error al actualitzar el jugador:", error)
    
