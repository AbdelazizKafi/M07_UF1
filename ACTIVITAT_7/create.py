# Importo les  funcions del fitxer per poder accedir a la bbdd.
from conn import conn, connection

# Funció per crear nous registres a la taula jugadors. 
# Selecciono les columnes que vull, en aquest totes i faig el try-except.
# Si la connexió falla o s'introdueix un valor no vàlid, donarà error. 
# Si tot es correcte mostrarà un text que ho confirma.
def crear_jugador(abreviacio, nom, equip, posicio, gols, trofeus):
    sql = '''
    INSERT INTO JUGADORS (abreviacio, nom, equip, posicio, gols, trofeus)
    VALUES (%s, %s, %s, %s, %s, %s)
    '''
    try:
        connection.execute(sql, (abreviacio, nom, equip, posicio, gols, trofeus))
        conn.commit()
        print("Jugador creat correctament.")
    except Exception as error:
        print("Error al crear el jugador:", error)
    
